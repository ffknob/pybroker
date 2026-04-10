from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID, uuid4

from pybroker.constant import text
from pybroker.ui.component.input import (
    TextInput,
    TextInputOptions,
    SelectInput,
    SelectInputOptions,
    IntegerInput,
    IntegerInputOptions,
    FloatInput,
    FloatInputOptions,
)
from pybroker.ui.screen.form_screen import FormScreen, FormScreenState
from pybroker.enums import OrderSide, ExecutionType, OrderStatus, TimeInForce
from pybroker.schema import User, Order


@dataclass(frozen=True)
class RegisterOrderScreenState(FormScreenState):
    pass


class RegisterOrderScreen(FormScreen[RegisterOrderScreenState, Order]):
    def __init__(self, state: RegisterOrderScreenState):
        super().__init__(state)

    def _get_ticker(self) -> str:
        text_input_options: TextInputOptions = TextInputOptions(label=text.TICKER)
        text_input_return = TextInput(options=text_input_options).render()

        return text_input_return

    def _get_side(self) -> OrderSide:
        select_input_options: SelectInputOptions = SelectInputOptions(
            label=text.SIDE, choices=OrderSide.values()
        )
        select_input_return = SelectInput(options=select_input_options).render()

        return OrderSide(select_input_return)

    def _get_execution_type(self) -> ExecutionType:
        select_input_options: SelectInputOptions = SelectInputOptions(
            label=text.EXECUTION_TYPE, choices=ExecutionType.values()
        )
        select_input_return = SelectInput(options=select_input_options).render()

        return ExecutionType(select_input_return)

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

    def render_content(self) -> None:
        pass

    def interaction(self) -> Order:
        id: UUID = uuid4()
        investor_id: UUID = uuid4()

        ticker: str = self._get_ticker()

        asset_id: UUID = uuid4()
        side: OrderSide = self._get_side()
        execution_type: ExecutionType = self._get_execution_type()
        status: OrderStatus = OrderStatus.PENDING

        quantity: int = self._get_quantity()
        executed: int = 0
        limit_price: Decimal = Decimal(self._get_limit_price())
        stop_price: Decimal = Decimal(self._get_stop_price())
        time_in_force: TimeInForce = self._get_time_in_force()

        trailing_amount: Decimal | None = None
        average_executed_price: Decimal | None = None

        now: datetime = datetime.now()

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
