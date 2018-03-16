"""
Module for BaseModel.

Author: Brendan Jones, GitHub: BrendanJones44
"""

from models.error import ErrorTypes

class BaseModel(object):
    """
    BaseModel represents the base object that all models in this application
    should extend.

    BaseModel
    + errors : dictionary of models.error.ErrorType: [models.error.Error]
    ---------
    + add_error : add error to errors dictionary
    + has_errors : tell whether the model has errors
    + error_msg : get the error message for the model
    """
    def __init__(self):
        self.errors = {}

    def add_error(self, error_type, error):
        """
        add_error adds the error to appropriate place in errors hash

        :param errors: the hash of {error_type:[error]} 's
        :param error_type: the type of error
        :param error: the error to add
        :return: none. Adds error to errors
        """
        if error_type in self.errors.keys():
            self.errors[error_type].append(error)
        else:
            self.errors[error_type] = [error]

    def has_errors(self):
        """
        has_errors tells whether or not the model has errors in the errors dict
        :return: true if model has errors, false otherwise.
        """
        return len(self.errors) > 0

    def error_msg(self):
        """
        error_msg builds and returns the error_msg string based off which
        errors exist in the errors hash
        :return:
        """
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
