from dataclasses import dataclass

from pybroker.constant.text import LIST_ORDERS_SCREEN_TITLE
from pybroker.ui.screen import BaseScreen, BaseScreenState
from pybroker.schema import User, Order


@dataclass
class ListOrdersScreenState(BaseScreenState):
    orders: list[Order]


class ListOrdersScreen(BaseScreen[ListOrdersScreenState, None]):
    def __init__(self, state: ListOrdersScreenState | None = None):
        super().__init__(LIST_ORDERS_SCREEN_TITLE, state)

    def render_content(self) -> None:
        if self.state and len(self.state.orders) > 1:
            orders: list[Order] = self.state.orders

            print(f"Quantidade de ordens: {len(orders)}")

        else:
            print("Sem ordens")

    def interaction(self) -> None:
        pass
