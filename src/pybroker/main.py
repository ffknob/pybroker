import asyncio

from pybroker.model import MenuOption
from pybroker.model.credentials import Credentials
from pybroker.provider.auth import (
    AbstractAuthenticationProvider,
    UsernamePasswordAuthProvider,
)
from pybroker.service import AuthService, AbstractOrderService, OrderService
from pybroker.repository import (
    AbstractOrderRepository,
    CsvOrderRepository,
)  # MemoryOrderRepository
from pybroker.ui.component import ErrorMessage
from pybroker.ui.screen import LoginScreen, MainMenuScreen


async def async_main() -> None:
    auth_provider: AbstractAuthenticationProvider = UsernamePasswordAuthProvider()
    auth_service: AuthService = AuthService(auth_provider)

    is_authenticated: bool = False
    while not is_authenticated:
        credentials: Credentials = LoginScreen().execute()

        is_authenticated = auth_service.login(credentials)

        if not is_authenticated:
            ErrorMessage().render(options={"message": "Informações incorretas"})

    # order_repository: AbstractOrderRepository = MemoryOrderRepository()
    order_repository: CsvOrderRepository = CsvOrderRepository(file="orders.csv")
    await order_repository.load()

    order_service: AbstractOrderService = OrderService(repository=order_repository)
    main_menu_screen: MainMenuScreen = MainMenuScreen(order_service=order_service)

    while True:
        item_menu_selecionado: MenuOption = main_menu_screen.execute()

        await item_menu_selecionado.action()


def main() -> None:
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
