from pybroker.model.credentials import Credentials
from pybroker.provider.auth import (
    AbstractAuthenticationProvider,
    UsernamePasswordAuthProvider,
)
from pybroker.service.auth import AuthService
from pybroker.model import MenuOption
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

    menu: list[MenuOption] = [
        MenuOption(
            order=1,
            name="REGISTRAR",
            description="Registrar ordem",
            icon="📝",
            action=lambda: print("Registrar ordem"),
        ),
        MenuOption(
            order=2,
            name="CONSULTAR",
            description="Consultar ordens",
            icon="🔍",
            action=lambda: print("Consultar ordens"),
        ),
        MenuOption(
            order=3,
            name="ALTERAR",
            description="Alterar ordem",
            icon="✏️",
            action=lambda: print("Alterar ordem"),
        ),
        MenuOption(
            order=4,
            name="CANCELAR",
            description="Cancelar ordem",
            icon="❌",
            action=lambda: print("Cancelar ordem"),
        ),
        MenuOption(
            order=9,
            name="SAIR",
            description="Sair",
            icon="🚪",
            action=lambda: exit(0),
        ),
    ]

    menu_screen: MenuScreen = MenuScreen()

    while True:
        item_menu_selecionado: int = menu_screen.execute(menu)

        item_menu_selecionado.action()


if __name__ == "__main__":
    main()
