from enum import Enum


class UserProfile(str, Enum):
    ADMIN = "admin"
    OPERATOR = "operator"
    CLIENT = "client"
