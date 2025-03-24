from enum import StrEnum, IntEnum, auto


class EmployeeType(StrEnum):
    ChiefExecutiveOfficer = auto()
    Designer = auto()
    Developer = auto()
    HrManager = auto()
    LeadDeveloper = auto()
    Manager = auto()
    Marketer = auto()
    OutsourcingExecutive = auto()
    Recruiter = auto()
    Researcher = auto()
    SalesExecutive = auto()
    Supporter = auto()
    SysAdmin = auto()

    def type_map(employee_str: str):
        return


class EmployeeLevel(StrEnum):
    BEGINNER = auto()
    INTERMEDIATE = auto()
    EXPERT = auto()


class Employee:
    def __init__(self, name: str, type: EmployeeType, level: EmployeeLevel):
        self.name = name
        self.type = type
        self.level = level
