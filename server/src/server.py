import gspread
from flask import Flask, render_template, request, jsonify
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

    resp_obj = {}
    errors = {}

    try:
        req_data["term"]
    except:
        add_error(errors, "missing parameter", "term")
    try:
        req_data["year"]
    except:
        add_error(errors, "missing parameter", "year")
        
    if len(errors) == 0:
        return "created", 201
    else:
        error_msg = ""
        for error_type, error_list in errors.items():
            if error_type == "missing parameter":
                if len(error_list) > 1:
                    error_msg += "missing parameters:"
                    for i in range(len(error_list)):
                        error_msg += " " + error_list[i] + ("," if (i != len(error_list) - 1) else "")
                elif len(error_list) == 1:
                    error_msg += "missing parameter:" + error_list[0]
        resp_obj["message"] = error_msg
        return jsonify(resp_obj), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


def add_error(errors, error_type, error):
    """
    add_error to appropriate place in errors hash

    :param errors: the hash of {error_type:[error]} 's
    :param error_type: the type of error
    :param error: the error to add
    :return: none. Adds error to errors
    """
    if error_type in errors.keys():
        errors[error_type].append(error)
    else:
        errors[error_type] = [error]