from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from rich.console import Console
from rich.table import Table

from pybroker.constant import text
from pybroker.ui.component.input import (
    SelectInput,
    SelectInputOptions,
    IntegerInput,
    IntegerInputOptions,
    FloatInput,
    FloatInputOptions,
)
from pybroker.ui.component.display import KeyValueDisplay, KeyValueDisplayOptions
from pybroker.ui.screen.form.form_screen import FormScreen, FormScreenState
from pybroker.enums import OrderSide, ExecutionType, OrderStatus, TimeInForce
from pybroker.schema import Order
from pybroker.constant import style

console = Console()


@dataclass(frozen=True)
class UpdateOrderScreenState(FormScreenState):
    orders: list[Order]


class UpdateOrderScreen(FormScreen[UpdateOrderScreenState, Order | None]):
    def __init__(self, state: UpdateOrderScreenState):
        super().__init__(state)

    def _get_time_in_force(self) -> TimeInForce:
        select_input_options: SelectInputOptions = SelectInputOptions(
            label=text.TIME_IN_FORCE, choices=TimeInForce.values()
        )
        select_input_return = SelectInput(options=select_input_options).render()

        return TimeInForce(select_input_return)

    def _get_quantity(self) -> int:
        integer_input_options: IntegerInputOptions = IntegerInputOptions(
            label=text.QUANTITY
        )
        integer_input_return = IntegerInput(options=integer_input_options).render()

        return integer_input_return

    def _get_limit_price(self) -> float:
        float_input_options: FloatInputOptions = FloatInputOptions(
            label=text.LIMIT_PRICE
        )
        float_input_return = FloatInput(options=float_input_options).render()

        return float_input_return

    def _get_stop_price(self) -> float:
        float_input_options: FloatInputOptions = FloatInputOptions(
            label=text.STOP_PRICE
        )
        float_input_return = FloatInput(options=float_input_options).render()

        return float_input_return

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

    def _render_order_frozen_values(self, order: Order) -> None:
        KeyValueDisplay(
            KeyValueDisplayOptions(
                key=text.TICKER,
                value=order.ticker,
                key_style=style.KEY_STYLE,
                value_style=style.VALUE_STYLE,
            )
        ).render()

        KeyValueDisplay(
            KeyValueDisplayOptions(
                key=text.SIDE,
                value=order.side.value,
                key_style=style.KEY_STYLE,
                value_style=style.VALUE_STYLE,
            )
        ).render()

        KeyValueDisplay(
            KeyValueDisplayOptions(
                key=text.EXECUTION_TYPE,
                value=order.execution_type.value,
                key_style=style.KEY_STYLE,
                value_style=style.VALUE_STYLE,
            )
        ).render()

        KeyValueDisplay(
            KeyValueDisplayOptions(
                key=text.STATUS,
                value=order.status.value,
                key_style=style.KEY_STYLE,
                value_style=style.VALUE_STYLE,
            )
        ).render()

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

            print("\n")

            order: Order = self.numbered_orders[selected_order]

            id: UUID = order.id
            investor_id: UUID = order.investor_id
            ticker: str = order.ticker
            asset_id: UUID = order.asset_id
            side: OrderSide = order.side
            execution_type: ExecutionType = order.execution_type
            status: OrderStatus = order.status
            executed: int = 0
            trailing_amount: Decimal | None = None
            average_executed_price: Decimal | None = None
            now: datetime = datetime.now()

            self._render_order_frozen_values(order)

            quantity: int = self._get_quantity()
            limit_price: Decimal = Decimal(self._get_limit_price())
            stop_price: Decimal = Decimal(self._get_stop_price())
            time_in_force: TimeInForce = self._get_time_in_force()

            return Order(
                id=id,
                investor_id=investor_id,
                asset_id=asset_id,
                ticker=ticker,
                side=side,
                execution_type=execution_type,
                status=status,
                quantity=quantity,
                executed_quantity=executed,
                limit_price=limit_price,
                stop_price=stop_price,
                trailing_amount=trailing_amount,
                average_executed_price=average_executed_price,
                time_in_force=time_in_force,
                created_at=now,
                updated_at=now,
                deleted_at=None,
            )
