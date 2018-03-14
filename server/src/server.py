import gspread
from flask import Flask, render_template, request, jsonify
from validations.validate_models import validate_term
from models.term import Term
from oauth2client.service_account import ServiceAccountCredentials
app = Flask(__name__)

@app.route('/')
def hello():
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    classes_sheet = client.open('gpa_calc_backend').sheet1
    classes = classes_sheet.get_all_records()
    return render_template('index.html', classes=classes)

@app.route('/terms/new', methods=['POST'])
def create_term():
    req_data = request.get_json()

    resp_obj = {}
    term = Term(req_data)


    if term.has_errors():
        resp_obj["message"] = term.error_msg()
        return jsonify(resp_obj), 400
    else:
        return "created", 201


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
