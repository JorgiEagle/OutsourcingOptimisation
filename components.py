from enum import StrEnum, auto
from employee import EmployeeLevel, EmployeeType


class ComponentType(StrEnum):
    COMPONENT = auto()
    MODULE = auto()
    SERVER = auto()


class BaseComponent:
    def __init__(self, name: str, component_type: ComponentType, cost: int, employee_type: EmployeeType,
                 employee_level: EmployeeLevel):
        self.name = name
        self.component_type = component_type
        self.cost = cost
        self.employee_type = employee_type
        self.employee_level = employee_level


class Component(BaseComponent):
    def __init__(self, name: str, cost: int, employee_type: EmployeeType, employee_level: EmployeeLevel):
        super().__init__(name, ComponentType.COMPONENT, cost, employee_type, employee_level)


class Module(BaseComponent):
    def __init__(self, name: str, cost: int, employee_type: EmployeeType, employee_level: EmployeeLevel):
        super().__init__(name, ComponentType.MODULE, cost, employee_type, employee_level)
