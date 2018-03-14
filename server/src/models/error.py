from enum import Enum

class ErrorTypes(Enum):
    MISSING_PARAM = "missing parameter"
    BAD_DATA = "must be integer"

class Error(object):
    def __init__(self, target, target_message):
        self.target = target
        self.target_message = target_message