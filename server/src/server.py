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

@APP.route('/')
def hello():
    """
    Display the data from the google sheets backend

    :return: the rendered index.html template
    """
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'client_secret.json', scope)
    client = gspread.authorize(creds)
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

    return "created", 201


if __name__ == "__main__":
    APP.run(host='0.0.0.0', debug=True)
