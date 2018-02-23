from enum import Enum

class SemesterTypes(Enum):
    SPRING = "Spring"
    SUMMER = "Summer"
    FALL = "Fall"

class Term(object):
    def __init__(self, semester_type, year):
        if type(year) is int:
            try:
                self.semester_type = SemesterTypes(semester_type)
            except:
                raise ValueError(str(semester_type) + ' is not a valid semester')
            self.year = year
        else:
            raise ValueError(str(year)  + ' is not an integer')
