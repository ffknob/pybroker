from uuid import UUID
from datetime import datetime
from pydantic import SecretStr

from pybroker.enums.user_profile import UserProfile
from pybroker.provider.auth import AbstractAuthenticationProvider
from pybroker.model import Credentials
from pybroker.schema import User


class UsernamePasswordAuthProvider(AbstractAuthenticationProvider):
    def authenticate(self, credentials: Credentials) -> bool:
        # TODO: retrieve user from repository
        user: User = User(
            id=UUID("0230dc7b-6041-4805-a5e4-ed793d5a0062"),
            name="Flávio Knob",
            email="ffknob@gmail.com",
            password=SecretStr("123456"),
            profile=UserProfile.CLIENT,
            active=True,
            created_at=datetime.fromisoformat("2024-06-01T00:00:00Z"),
            updated_at=datetime.fromisoformat("2024-06-01T00:00:00Z"),
        )

        return (
            credentials.username == user.email
            and SecretStr(credentials.password) == user.password
        )
