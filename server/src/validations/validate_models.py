from enum import Enum

class ErrorTypes(Enum):
    MISSING_PARAM = "missing parameter"
    NOT_INT = "must be integer"

def validate_term(req_data):
    errors = {}
    data_has_year = True

    try:
        req_data["term"]
    except:
        add_error(errors, ErrorTypes.MISSING_PARAM, "term")
    try:
        req_data["year"]
    except:
        data_has_year = False
        add_error(errors, ErrorTypes.MISSING_PARAM, "year")

    if data_has_year:
        try:
            int(req_data["year"])
        except:
            add_error(errors, ErrorTypes.NOT_INT, "year")

    return create_error_message(errors)

def create_error_message(errors):
    """


    :param errors:
    :return:
    """
    error_msg = ""
    for error_type, error_list in errors.items():
        if error_type ==  ErrorTypes.MISSING_PARAM:
            if len(error_list) > 1:
                error_msg += "missing parameters:"
                for i in range(len(error_list)):
                    # Only add a comma if there is more data left
                    error_msg += " " + error_list[i] + \
                        ("," if (i != len(error_list) - 1) else "")
            elif len(error_list) == 1:
                error_msg += ErrorTypes.MISSING_PARAM.value + \
                             ": " + error_list[0]
        elif error_type == ErrorTypes.NOT_INT:
            error_msg += ErrorTypes.NOT_INT.value + \
                ": " + error_list[0]

    return error_msg

def add_error(errors, error_type, error):
    """
    add_error adds the error to appropriate place in errors hash

    :param errors: the hash of {error_type:[error]} 's
    :param error_type: the type of error
    :param error: the error to add
    :return: none. Adds error to errors
    """
    if error_type in errors.keys():
        errors[error_type].append(error)
    else:
        errors[error_type] = [error]
