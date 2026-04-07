from pybroker.model.credentials import Credentials
from pybroker.provider.auth import (
    AbstractAuthenticationProvider,
    UsernamePasswordAuthProvider,
)
from pybroker.service.auth import AuthService
from pybroker.model import MenuOption
from pybroker.ui.component import ErrorMessage
from pybroker.ui.screen import LoginScreen, MainMenuScreen


def main():
    auth_provider: AbstractAuthenticationProvider = UsernamePasswordAuthProvider()
    auth_service: AuthService = AuthService(auth_provider)

    is_authenticated: bool = False
    while not is_authenticated:
        credentials: Credentials = LoginScreen().execute()

        is_authenticated = auth_service.login(credentials)

        if not is_authenticated:
            ErrorMessage().render(options={"message": "Informações incorretas"})

    main_menu_screen: MainMenuScreen = MainMenuScreen()

    while True:
        item_menu_selecionado: MenuOption = main_menu_screen.execute()

        item_menu_selecionado.action()


if __name__ == "__main__":
    main()
