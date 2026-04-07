from pydantic import EmailStr, SecretStr

from pybroker.enums.user_profile import UserProfile
from pybroker.schema.base import BaseSchema


class User(BaseSchema):
    name: str
    email: EmailStr
    password: SecretStr
    profile: UserProfile
    active: bool
