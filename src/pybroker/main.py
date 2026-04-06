from pybroker.model.credentials import Credentials
from pybroker.provider.auth import (
    AbstractAuthenticationProvider,
    UsernamePasswordAuthProvider,
)
from pybroker.service.auth import AuthService
from pybroker.ui.component import ErrorMessage
from pybroker.ui.screen import LoginScreen, MenuScreen


def main():
    auth_provider: AbstractAuthenticationProvider = UsernamePasswordAuthProvider()
    auth_service: AuthService = AuthService(auth_provider)

    is_authenticated: bool = False
    while not is_authenticated:
        credentials: Credentials = LoginScreen().execute()

        is_authenticated = auth_service.login(credentials)

        if not is_authenticated:
            ErrorMessage().render(options={"message": "Informações incorretas"})

    opcoes_menu = {
        1: "Registrar ordem",
        2: "Consultar ordens",
        3: "Alterar ordem",
        4: "Cancelar ordem",
        9: "Sair",
    }

    MenuScreen().execute(options=opcoes_menu)


if __name__ == "__main__":
    main()
