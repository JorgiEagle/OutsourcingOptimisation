from enum import StrEnum, auto
from typing import List
from components import BaseComponent
from employee import EmployeeLevel
from dataclasses import dataclass


class FeatureTypes(StrEnum):
    USER = auto()
    REVENUE = auto()
    ENHANCEMENT = auto()


@dataclass
class FeatureRequirement:
    component: BaseComponent
    quantity: int


class BaseFeature:
    def __init__(self, name: str, level: EmployeeLevel, feature_type: FeatureTypes,
                 requirements: List[FeatureRequirement]):
        self.name = name
        self.level = level,
        self.type = feature_type
        self.requirements = requirements


class UserFeature(BaseFeature):
    def __init__(self, name: str, level: EmployeeLevel, requirements: List[FeatureRequirement]):
        super().__init__(name, level, FeatureTypes.USER, requirements)


class RevenueFeature(BaseFeature):
    def __init__(self, name: str, level: EmployeeLevel, disatisfaction: int):
        super().__init__(name, level, FeatureTypes.REVENUE, None)
        self.disatisfaction = disatisfaction


class EnhancementFeature(BaseFeature):
    def __init__(self, name: str, level: EmployeeLevel, requirements: List[FeatureRequirement]):
        super().__init__(name, level, FeatureTypes.ENHANCEMENT, requirements)
