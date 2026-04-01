from pybroker.model.credentials import Credentials
from pybroker.provider.auth import (
    AbstractAuthenticationProvider,
    UsernamePasswordAuthProvider,
)
from pybroker.service.auth import AuthService
from pybroker.ui.screen import LoginScreen


def main():
    credentials: Credentials = LoginScreen().execute()

    auth_provider: AbstractAuthenticationProvider = UsernamePasswordAuthProvider()
    auth_service: AuthService = AuthService(auth_provider)

    if auth_service.login(credentials):
        print("Login successful")

    else:
        print("Login failed")


if __name__ == "__main__":
    main()
