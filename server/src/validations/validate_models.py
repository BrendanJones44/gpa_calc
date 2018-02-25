from enum import Enum

class ErrorTypes(Enum):
    MISSING_PARAM = "missing parameter"

def validate_term(req_data):
    errors = {}

    try:
        req_data["term"]
    except:
        add_error(errors, ErrorTypes.MISSING_PARAM, "term")
    try:
        req_data["year"]
    except:
        add_error(errors,ErrorTypes.MISSING_PARAM, "year")

    return create_error_message(errors)

def create_error_message(errors):
    error_msg = ""
    for error_type, error_list in errors.items():
        if error_type ==  ErrorTypes.MISSING_PARAM:
            if len(error_list) > 1:
                error_msg += "missing parameters:"
                for i in range(len(error_list)):
                    error_msg += " " + error_list[i] + (
                        "," if (i != len(error_list) - 1) else "")
            elif len(error_list) == 1:
                error_msg += ErrorTypes.MISSING_PARAM.value + ": " + error_list[0]
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
