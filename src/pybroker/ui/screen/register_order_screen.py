from datetime import datetime
from decimal import Decimal
from uuid import UUID, uuid4

from pybroker.constant.text import (
    TICKER,
    STOP_PRICE,
    LIMIT_PRICE,
    QUANTITY,
    REGISTER_ORDER_SCREEN_TITLE,
    SIDE,
    EXECUTION_TYPE,
    TIME_IN_FORCE,
)
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
from pybroker.ui.screen.form_screen import FormScreen
from pybroker.enums import OrderSide, ExecutionType, OrderStatus, TimeInForce
from pybroker.schema import User, Order


class RegisterOrderScreen(FormScreen[User, Order]):
    def __init__(self):
        super().__init__(REGISTER_ORDER_SCREEN_TITLE)

    def _get_ticker(self) -> str:
        text_input_options: TextInputOptions = TextInputOptions(label=TICKER)
        text_input_return = TextInput().render(text_input_options)

        return text_input_return

    def _get_side(self) -> OrderSide:
        select_input_options: SelectInputOptions = SelectInputOptions(
            label=SIDE, choices=OrderSide.values()
        )
        select_input_return = SelectInput().render(select_input_options)

        return OrderSide(select_input_return)

    def _get_execution_type(self) -> ExecutionType:
        select_input_options: SelectInputOptions = SelectInputOptions(
            label=EXECUTION_TYPE, choices=ExecutionType.values()
        )
        select_input_return = SelectInput().render(select_input_options)

        return ExecutionType(select_input_return)

    def _get_time_in_force(self) -> TimeInForce:
        select_input_options: SelectInputOptions = SelectInputOptions(
            label=TIME_IN_FORCE, choices=TimeInForce.values()
        )
        select_input_return = SelectInput().render(select_input_options)

        return TimeInForce(select_input_return)

    def _get_quantity(self) -> int:
        integer_input_options: IntegerInputOptions = IntegerInputOptions(label=QUANTITY)
        integer_input_return = IntegerInput().render(integer_input_options)

        return integer_input_return

    def _get_limit_price(self) -> float:
        float_input_options: FloatInputOptions = FloatInputOptions(label=LIMIT_PRICE)
        float_input_return = FloatInput().render(float_input_options)

        return float_input_return

    def _get_stop_price(self) -> float:
        float_input_options: FloatInputOptions = FloatInputOptions(label=STOP_PRICE)
        float_input_return = FloatInput().render(float_input_options)

        return float_input_return

    def render_content(self) -> None:
        pass

    def interaction(self, state: User | None = None) -> Order:
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

        now: datetime = datetime.now()

        return Order(
            id=id,
            investor_id=investor_id,
            asset_id=asset_id,
            side=side,
            execution_type=execution_type,
            status=status,
            quantity=quantity,
            executed_quantity=executed,
            limit_price=limit_price,
            stop_price=stop_price,
            time_in_force=time_in_force,
            created_at=now,
            updated_at=now,
        )
