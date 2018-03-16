"""
Module for errors within modules for this application.

Author: Brendan Jones, GitHub: BrendanJones44
"""

from enum import Enum

class ErrorTypes(Enum):
    """
    ErrorTypes is an Enum of various classes of errors the model can have
    """
    MISSING_PARAM = "missing parameter"
    BAD_DATA = "must be integer"

class Error(object):
    """
    Error represents an error on the actual model

    Error
    + target : the field/target that the error is caused by
    + target_message : the message about the error's target
    -----
    """
    def __init__(self, target, target_message):
        self.target = target
        self.target_message = target_message
