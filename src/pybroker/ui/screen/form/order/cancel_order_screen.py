from dataclasses import dataclass

from rich.console import Console
from rich.table import Table

from pybroker.constant import text
from pybroker.ui.component.input import IntegerInput, IntegerInputOptions
from pybroker.ui.screen import BaseScreen, BaseScreenState
from pybroker.schema import Order

console = Console()


@dataclass(frozen=True)
class CancelOrderScreenState(BaseScreenState):
    orders: list[Order]


class CancelOrderScreen(BaseScreen[CancelOrderScreenState, Order | None]):
    def __init__(self, state: CancelOrderScreenState):
        super().__init__(state)

        self.numbered_orders: dict[int, Order] = {}

    def _render_orders_table(self) -> None:
        if self.state and len(self.state.orders) > 0:
            orders: list[Order] = self.state.orders

            self.numbered_orders = {i + 1: order for i, order in enumerate(orders)}

            table = Table(show_header=True, header_style="bold")
            table.add_column("#")
            table.add_column(text.LIST_ORDERS_TABLE_COLUMN_TICKER)
            table.add_column(text.LIST_ORDERS_TABLE_COLUMN_SIDE)
            table.add_column(text.LIST_ORDERS_TABLE_COLUMN_EXECUTION_TYPE)
            table.add_column(text.LIST_ORDERS_TABLE_COLUMN_TIME_IN_FORCE)
            table.add_column(text.LIST_ORDERS_TABLE_COLUMN_QUANTITY, justify="right")
            table.add_column(text.LIST_ORDERS_TABLE_COLUMN_LIMIT_PRICE, justify="right")
            table.add_column(text.LIST_ORDERS_TABLE_COLUMN_STOP_PRICE, justify="right")
            table.add_column(text.LIST_ORDERS_TABLE_COLUMN_CREATED_AT)
            table.add_column(text.LIST_ORDERS_TABLE_COLUMN_UPDATED_AT)

            for i, order in self.numbered_orders.items():
                table.add_row(
                    str(i),
                    str(order.ticker),
                    order.side.value,
                    order.execution_type.value,
                    order.time_in_force.value,
                    str(order.quantity),
                    str(order.limit_price) if order.limit_price is not None else "-",
                    str(order.stop_price) if order.stop_price is not None else "-",
                    order.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                    order.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
                )

            console.print(table)

    def render_content(self) -> None:
        if self.state and len(self.state.orders) > 0:
            self._render_orders_table()

        else:
            print(text.MESSAGE_NO_ORDERS_REGISTERED)

        print("\n")

    def interaction(self) -> Order | None:
        if self.state and len(self.state.orders) > 0:
            selected_order: int = IntegerInput(
                IntegerInputOptions(label=f"{text.ORDER} #")
            ).render()

            return self.numbered_orders[selected_order]
