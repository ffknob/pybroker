from pybroker.provider.auth import AbstractAuthenticationProvider
from pybroker.model import Credentials


class AuthService:
    def __init__(self, auth_provider: AbstractAuthenticationProvider):
        self.auth_provider = auth_provider

    def login(self, credentials: Credentials) -> bool:
        return self.auth_provider.authenticate(credentials)
