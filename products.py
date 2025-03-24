from features import BaseFeature

from enum import StrEnum, auto
from typing import List


class AudienceGroups(StrEnum):
    AGE_YOUNG = auto()
    AGE_MID = auto()
    AGE_OLD = auto()
    BUSINESS = auto()
    ENTERTAINMENT = auto()
    FAMILY = auto()
    FASHION = auto()
    FOOD = auto()
    SHOPPING = auto()
    SPORTS = auto()
    TECHNOLOGY = auto()
    TRAVEL = auto()


class Product:
    def __init__(self, name: str, features: List[BaseFeature], audience: List[AudienceGroups]):
        self.name = name
        self.features = features
        self.intended_audience = audience
