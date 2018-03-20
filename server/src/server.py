"""
Module to represent the Flask server handling the back-end logic and interaction
with Google Spreadsheets.

Author: Brendan Jones, GitHub: BrendanJones44
"""

import gspread
from flask import Flask, render_template, request, jsonify
from oauth2client.service_account import ServiceAccountCredentials

from models.term import Term


APP = Flask(__name__)
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'client_secret.json', scope)
client = gspread.authorize(creds)


@APP.route('/')
def hello():
    """
    Display the data from the google sheets backend

    :return: the rendered index.html template
    """
    classes_sheet = client.open('gpa_calc_backend').sheet1
    classes = classes_sheet.get_all_records()
    return render_template('index.html', classes=classes)

@APP.route('/terms/new', methods=['POST'])
def create_term():
    """
    Create a term from request body data

    :return: 400 response with message if request invalid otherwise
             201 response stating it's been created
    """
    req_data = request.get_json()

    resp_obj = {}
    term = Term(req_data)

    if term.has_errors():
        resp_obj["message"] = term.error_msg()
        return jsonify(resp_obj), 400

    else:
        terms_sheet = client.open('gpa_calc_backend').sheet1
        terms_sheet.insert_row([term.year, term.semester_type])
        return "created", 201

@APP.route('/terms/<int:term_id>', methods=['GET'])
def get_term_by_id():
    """
    Get a term from it's id

    :return:
    """


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
