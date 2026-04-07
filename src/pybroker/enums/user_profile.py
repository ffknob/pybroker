from pybroker.enums.base import BaseEnum


class UserProfile(BaseEnum):
    ADMIN = "admin"
    OPERATOR = "operator"
    CLIENT = "client"
