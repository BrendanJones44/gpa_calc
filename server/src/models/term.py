from enum import Enum
from models.error import Error, ErrorTypes

class SemesterTypes(Enum):
    SPRING = "Spring"
    SUMMER = "Summer"
    FALL = "Fall"

class Term(object):
    def __init__(self, req_data):
        self.errors = {}
        data_has_year = True
        data_has_semester = True

        # Grab the semester if it's in the request
        try:
            semester_type = req_data["term"]
        except:
            error = Error("term", "term is required")
            add_error(self.errors, ErrorTypes.MISSING_PARAM, error)
            data_has_semester = False

        # Grab the year if it's in the request
        try:
            year = req_data["year"]
        except:
            data_has_year = False
            error = Error("year", "year is required")
            add_error(self.errors, ErrorTypes.MISSING_PARAM, error)

        if data_has_year:

            # Make sure the year is an integer
            try:
                self.year = int(req_data["year"])
            except:
                error = Error("year", "year must be integer")
                add_error(self.errors, ErrorTypes.BAD_DATA, error)

        if data_has_semester:

            # Make sure the semester type is valid
            try:
                self.semester_type = SemesterTypes(semester_type)
            except:
                error = Error("term", "semester not valid")
                add_error(self.errors, ErrorTypes.BAD_DATA, error)

    def error_msg(self):
        error_msg = ""
        for error_type, error_list in self.errors.items():
            if error_type == ErrorTypes.MISSING_PARAM:

                # Check for plurization
                if len(error_list) > 1:
                    error_msg += "missing parameters:"
                    for i in range(len(error_list)):

                        # Only add a comma if there is more data left
                        error_msg += " " + error_list[i].target + \
                                     ("," if (i != len(error_list) - 1) else "")
                elif len(error_list) == 1:
                    error_msg += ErrorTypes.MISSING_PARAM.value + \
                                 ": " + error_list[0].target
            elif error_type == ErrorTypes.BAD_DATA:
                error_msg += ErrorTypes.BAD_DATA.value + \
                             ": " + error_list[0].target

        return error_msg

    def has_errors(self):
        return len(self.errors) > 0

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