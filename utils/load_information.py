from pathlib import Path
from enum import Enum
from copy import deepcopy

from components import Component, Module
from employee import EmployeeLevel, EmployeeType
from features import UserFeature, RevenueFeature, EnhancementFeature, FeatureRequirement
from products import Product, AudienceGroups
import json


DATA_FILE_LOCATION = Path.cwd() / Path("/data/game_values.JSON")
data = json.load(DATA_FILE_LOCATION)


def get_enum_from_string(enum_class: Enum, input_string: str):
    for member in enum_class:
        if input_string.lower() == member.value:
            return member
    else:
        raise KeyError(f"No match found for {input_string}")


def component_constructor(entry):
    match entry['type']:
        case 'Component':
            return Component
        case 'Module':
            return Module


def feature_constructor(entry):
    match entry['categoryName']:
        case 'Users':
            return UserFeature
        case 'Revenue':
            return RevenueFeature
        case 'Enhancemet':
            return EnhancementFeature


def construct_component(entry):
    constructor = component_constructor(entry)
    return constructor(entry['name'], entry['produceHours'],
                       get_enum_from_string(EmployeeType, entry['employeeTypeName']),
                       get_enum_from_string(EmployeeLevel, entry['employeeLevel'])
                       )


def construct_feature(entry, all_components):
    constructor = feature_constructor(entry)
    kwargs = {
        "name": entry['name'],
        "level": get_enum_from_string(EmployeeLevel, entry['level']),
    }
    if constructor is RevenueFeature:
        kwargs['disatisfaction'] = entry['disatisfaction']
    else:
        kwargs['requirements'] = [FeatureRequirement(deepcopy(all_components[requirement]), quantity)
                                  for requirement, quantity in entry['requirements'].items()]
    return constructor(**kwargs)


def construct_product(entry, all_features):
    feature_objects = [deepcopy(all_features['feature']) for feature in entry['features']]
    audience_groups = [get_enum_from_string(AudienceGroups, audience) for audience in entry['audienceMatches']]
    return Product(entry['name'], feature_objects, audience_groups)


def load_information():
    components = {entry['name']: construct_component(entry) for entry in data['Components']}
    features = {entry['name']: construct_feature(entry, components) for entry in data['Features']}
    products = {entry['Name']: construct_product(entry, features) for entry in data['Products']}
    return components, features, products


if __name__ == '__main__':
    load_information()
