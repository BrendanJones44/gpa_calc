from flask import Flask, render_template, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

@app.route('/')
def hello():
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    classes_sheet = client.open('gpa_calc_backend').sheet1
    classes = classes_sheet.get_all_records()
    #print(classes)
    return render_template('index.html', classes=classes)

@app.route('/terms/new', methods=['POST'])
def create_term():
    req_data = request.get_json()
    error_message = ""
    resp_obj = {}
    try:
        req_data["term"]
    except:
        error_message +="missing parameter: term."
    if not error_message:
        return "created", 201
    else:
        resp_obj["message"] = error_message
        return jsonify(resp_obj), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


