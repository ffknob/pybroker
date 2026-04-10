from typing import Awaitable

from pybroker.ui.screen import (
    MenuScreen,
)
from pybroker.ui.screen.register_order_screen import (
    RegisterOrderScreen,
    RegisterOrderScreenState,
)
from pybroker.ui.screen.list_orders_screen import (
    ListOrdersScreen,
    ListOrdersScreenState,
)
from pybroker.ui.screen.cancel_order_screen import (
    CancelOrderScreen,
    CancelOrderScreenState,
)
from pybroker.enums import OrderStatus
from pybroker.model import MenuOption
from pybroker.schema import Order
from pybroker.service import AbstractOrderService
from pybroker.constant import text


class MainMenuScreen(MenuScreen):
    def __init__(self, order_service: AbstractOrderService):
        self.order_service = order_service

        menu: list[MenuOption] = [
            MenuOption(
                order=1,
                name="REGISTER_ORDER",
                description=text.MAIN_MENU_REGISTER_ORDER_OPTION,
                icon="📝",
                action=self._register_order_action,
            ),
            MenuOption(
                order=2,
                name="LIST_ORDERS",
                description=text.MAIN_MENU_LIST_ORDERS_OPTION,
                icon="🔍",
                action=self._list_orders_action,
            ),
            MenuOption(
                order=3,
                name="UPDATE_ORDER",
                description=text.MAIN_MENU_UPDATE_ORDER_OPTION,
                icon="✏️",
                action=self._update_order_action,
            ),
            MenuOption(
                order=4,
                name="CANCEL",
                description=text.MAIN_MENU_CANCEL_ORDER_OPTION,
                icon="❌",
                action=self._cancel_order_action,
            ),
            MenuOption(
                order=9,
                name="EXIT",
                description=text.MAIN_MENU_EXIT_OPTION,
                icon="🚪",
                action=self._exit_action,
            ),
        ]

        super().__init__(text.MAIN_MENU_SCREEN_TITLE, menu)

    async def _register_order_action(self) -> None:
        state: RegisterOrderScreenState = RegisterOrderScreenState(user=None)
        order: Order = RegisterOrderScreen(state=state).execute()

        await self.order_service.register(order)

    async def _list_orders_action(self) -> None:
        orders: list[Order] = await self.order_service.list()
        state: ListOrdersScreenState = ListOrdersScreenState(orders=orders)

        ListOrdersScreen(state=state).execute()

    async def _update_order_action(self) -> None:
        pass

    async def _cancel_order_action(self) -> None:
        orders: list[Order] = await self.order_service.list()
        pending_orders: list[Order] = [
            order for order in orders if order.status == OrderStatus.PENDING
        ]
        state: CancelOrderScreenState = CancelOrderScreenState(orders=pending_orders)

        order_to_be_cancelled: Order = CancelOrderScreen(state=state).execute()

        await self.order_service.cancel(order_to_be_cancelled)

    async def _exit_action(self) -> None:
        exit(0)
