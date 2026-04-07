from pybroker.ui.screen import MenuScreen, ScreenState
from pybroker.model import MenuOption
from pybroker.constant.text import (
    MAIN_MENU_SCREEN_TITLE,
    MAIN_MENU_REGISTER_ORDER_OPTION,
    MAIN_MENU_LIST_ORDERS_OPTION,
    MAIN_MENU_UPDATE_ORDER_OPTION,
    MAIN_MENU_CANCEL_ORDER_OPTION,
    MAIN_MENU_EXIT_OPTION,
)


class MainMenuScreen(MenuScreen):
    def __init__(self):
        menu: list[MenuOption] = [
            MenuOption(
                order=1,
                name="REGISTER_ORDER",
                description=MAIN_MENU_REGISTER_ORDER_OPTION,
                icon="📝",
                action=self._register_order_action,
            ),
            MenuOption(
                order=2,
                name="LIST_ORDERS",
                description=MAIN_MENU_LIST_ORDERS_OPTION,
                icon="🔍",
                action=self._list_orders_action,
            ),
            MenuOption(
                order=3,
                name="UPDATE_ORDER",
                description=MAIN_MENU_UPDATE_ORDER_OPTION,
                icon="✏️",
                action=self._update_order_action,
            ),
            MenuOption(
                order=4,
                name="CANCELAR",
                description=MAIN_MENU_CANCEL_ORDER_OPTION,
                icon="❌",
                action=self._cancel_order_action,
            ),
            MenuOption(
                order=9,
                name="EXIT",
                description=MAIN_MENU_EXIT_OPTION,
                icon="🚪",
                action=self._exit_action,
            ),
        ]

        super().__init__(MAIN_MENU_SCREEN_TITLE, menu)

    def _register_order_action(self) -> None:
        pass

    def _list_orders_action(self) -> None:
        pass

    def _update_order_action(self) -> None:
        pass

    def _cancel_order_action(self) -> None:
        pass

    def _exit_action(self) -> None:
        exit(0)

    def execute(self, state: ScreenState | None = None) -> MenuOption:
        return super().execute()
