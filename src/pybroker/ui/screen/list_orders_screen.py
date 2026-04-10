from dataclasses import dataclass

from rich.console import Console
from rich.table import Table

from pybroker.constant import text
from pybroker.ui.screen import BaseScreen, BaseScreenState
from pybroker.schema import Order


@dataclass(frozen=True)
class ListOrdersScreenState(BaseScreenState):
    orders: list[Order]


class ListOrdersScreen(BaseScreen[ListOrdersScreenState, None]):
    def __init__(self, state: ListOrdersScreenState):
        super().__init__(state)

    def _render_orders_table(self) -> None:
        if self.state and len(self.state.orders) > 0:
            orders: list[Order] = self.state.orders

            table = Table(show_header=True, header_style="bold")
            table.add_column(text.LIST_ORDERS_TABLE_COLUMN_TICKER)
            table.add_column(text.LIST_ORDERS_TABLE_COLUMN_SIDE)
            table.add_column(text.LIST_ORDERS_TABLE_COLUMN_EXECUTION_TYPE)
            table.add_column(text.LIST_ORDERS_TABLE_COLUMN_TIME_IN_FORCE)
            table.add_column(text.LIST_ORDERS_TABLE_COLUMN_STATUS)
            table.add_column(text.LIST_ORDERS_TABLE_COLUMN_QUANTITY, justify="right")
            table.add_column(
                text.LIST_ORDERS_TABLE_COLUMN_EXECUTED_QUANTITY, justify="right"
            )
            table.add_column(text.LIST_ORDERS_TABLE_COLUMN_LIMIT_PRICE, justify="right")
            table.add_column(text.LIST_ORDERS_TABLE_COLUMN_STOP_PRICE, justify="right")
            table.add_column(
                text.LIST_ORDERS_TABLE_COLUMN_AVERAGE_EXECUTED_PRICE, justify="right"
            )
            table.add_column(text.LIST_ORDERS_TABLE_COLUMN_CREATED_AT)
            table.add_column(text.LIST_ORDERS_TABLE_COLUMN_UPDATED_AT)

            for order in orders:
                table.add_row(
                    str(order.ticker),
                    order.side.value,
                    order.execution_type.value,
                    order.time_in_force.value,
                    order.status.value,
                    str(order.quantity),
                    str(order.executed_quantity),
                    str(order.limit_price) if order.limit_price is not None else "-",
                    str(order.stop_price) if order.stop_price is not None else "-",
                    str(order.average_executed_price)
                    if order.average_executed_price is not None
                    else "-",
                    order.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                    order.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
                )

            Console().print(table)

    def render_content(self) -> None:
        if self.state and len(self.state.orders) > 0:
            self._render_orders_table()

        else:
            print(text.MESSAGE_NO_ORDERS_REGISTERED)

    def interaction(self) -> None:
        pass
