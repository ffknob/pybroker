from typing import Iterator

from pybroker.ui.screen.form.order.register_order_screen import (
    RegisterOrderScreen,
    RegisterOrderScreenState,
)
from pybroker.ui.screen.form.order.list_orders_screen import (
    ListOrdersScreen,
    ListOrdersScreenState,
)
from pybroker.ui.screen.form.order.cancel_order_screen import (
    CancelOrderScreen,
    CancelOrderScreenState,
)
from pybroker.ui.component.message import SuccessMessage, SuccessMessageOptions
from pybroker.enums import OrderStatus
from pybroker.model import MenuOption
from pybroker.schema import Order
from pybroker.service import AbstractOrderService
from pybroker.constant import text, icon


class MainMenuOptions:
    def __init__(self, order_service: AbstractOrderService):
        self.order_service = order_service

        self.options: list[MenuOption] = [
            MenuOption(
                order=1,
                name="REGISTER_ORDER",
                description=text.MAIN_MENU_REGISTER_ORDER_OPTION,
                icon=icon.REGISTER,
                action=self._register_order_action,
            ),
            MenuOption(
                order=2,
                name="LIST_ORDERS",
                description=text.MAIN_MENU_LIST_ORDERS_OPTION,
                icon=icon.LIST,
                action=self._list_orders_action,
            ),
            MenuOption(
                order=3,
                name="UPDATE_ORDER",
                description=text.MAIN_MENU_UPDATE_ORDER_OPTION,
                icon=icon.UPDATE,
                action=self._update_order_action,
            ),
            MenuOption(
                order=4,
                name="CANCEL",
                description=text.MAIN_MENU_CANCEL_ORDER_OPTION,
                icon=icon.CANCEL,
                action=self._cancel_order_action,
            ),
            MenuOption(
                order=9,
                name="EXIT",
                description=text.MAIN_MENU_EXIT_OPTION,
                icon=icon.EXIT,
                action=self._exit_action,
            ),
        ]

    async def _register_order_action(self) -> None:
        state: RegisterOrderScreenState = RegisterOrderScreenState(
            title=text.REGISTER_ORDER_SCREEN_TITLE, icon=icon.REGISTER, show_title=True
        )
        order: Order = RegisterOrderScreen(state=state).execute()

        await self.order_service.register(order)

        SuccessMessage(
            SuccessMessageOptions(message=text.MESSAGE_ORDER_REGISTERED)
        ).render()

    async def _list_orders_action(self) -> None:
        orders: list[Order] = await self.order_service.list()
        state: ListOrdersScreenState = ListOrdersScreenState(
            title=text.LIST_ORDERS_SCREEN_TITLE,
            icon=icon.LIST,
            show_title=True,
            orders=orders,
        )

        ListOrdersScreen(state=state).execute()

    async def _update_order_action(self) -> None:
        SuccessMessage(
            SuccessMessageOptions(message=text.MESSAGE_ORDER_UPDATED)
        ).redner()

    async def _cancel_order_action(self) -> None:
        orders: list[Order] = await self.order_service.list()
        pending_orders: list[Order] = [
            order for order in orders if order.status == OrderStatus.PENDING
        ]
        state: CancelOrderScreenState = CancelOrderScreenState(
            title=text.CANCEL_ORDER_SCREEN_TITLE,
            icon=icon.CANCEL,
            show_title=True,
            orders=pending_orders,
        )

        order_to_be_cancelled: Order | None = CancelOrderScreen(state=state).execute()

        if order_to_be_cancelled:
            await self.order_service.cancel(order_to_be_cancelled)

            SuccessMessage(
                SuccessMessageOptions(message=text.MESSAGE_ORDER_CANCELLED)
            ).render()

    async def _exit_action(self) -> None:
        exit(0)

    def __iter__(self) -> Iterator[MenuOption]:
        return iter(self.options)
