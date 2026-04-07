from enum import Enum


class PersonType(str, Enum):
    INDIVIDUAL = "individual"
    CORPORATE = "corporate"
