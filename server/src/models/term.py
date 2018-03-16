"""
Module for the Term model for this application.

Author: Brendan Jones, GitHub: BrendanJones44
"""

from enum import Enum
from models.error import Error, ErrorTypes
from models.base_model import BaseModel

class SemesterTypes(Enum):
    """
    SemesterTypes is an Enum of acceptable Strings to represent semesters
    """
    SPRING = "Spring"
    SUMMER = "Summer"
    FALL = "Fall"

class Term(BaseModel):
    """
    Term represents the actual term a GPA or a class can belong to

    Term
    + semester_type : SemesterTypes representing the semester the term is in
    + year : the year the term was in
    ----
    """
    def __init__(self, req_data):
        """
        Create term object from an http request body's req_data.
        If any errors occur in creating the Term object, they will
        be attached to the errors dictionary

        :param req_data: the http request body as a dictionary
        """
        super().__init__()

        # Initally assume the data has a year and semester,
        # change to False otherwise.
        data_has_year = True
        data_has_semester = True

        # Grab the semester if it's in the request
        try:
            semester_type = req_data["term"]
        except KeyError:
            error = Error("term", "term is required")
            self.add_error(ErrorTypes.MISSING_PARAM, error)
            data_has_semester = False

        # Grab the year if it's in the request
        try:
            year = req_data["year"]
        except KeyError:
            data_has_year = False
            error = Error("year", "year is required")
            self.add_error(ErrorTypes.MISSING_PARAM, error)

        if data_has_year:

            # Make sure the year is an integer
            try:
                self.year = int(year)
            except ValueError:
                error = Error("year", "year must be integer")
                self.add_error(ErrorTypes.BAD_DATA, error)

        if data_has_semester:

            # Make sure the semester type is valid
            try:
                self.semester_type = SemesterTypes(semester_type)
            except ValueError:
                error = Error("term", "semester not valid")
                self.add_error(ErrorTypes.BAD_DATA, error)
