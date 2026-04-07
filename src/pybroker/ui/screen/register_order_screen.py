from datetime import datetime
from decimal import Decimal
from uuid import UUID, uuid4

from rich.prompt import Prompt

from pybroker.constant.text import REGISTER_ORDER_SCREEN_TITLE
from pybroker.constant.style import TEXT_INPUT
from pybroker.ui.screen.base_screen import BaseScreen
from pybroker.ui.screen.abstract_screen import ScreenState
from pybroker.ui.component import ErrorMessage
from pybroker.enums import OrderSide, ExecutionType, OrderStatus, TimeInForce
from pybroker.schema import Order


class RegisterOrderScreen(BaseScreen[None, Order]):
    def __init__(self):
        super().__init__(REGISTER_ORDER_SCREEN_TITLE)

    def _get_side(self) -> OrderSide:
        while True:
            input: str = Prompt.ask(
                f"[{TEXT_INPUT}]📧 Side ({OrderSide.values()}) [/{TEXT_INPUT}]"
            )

            if input in OrderSide.values():
                return OrderSide(input)

            else:
                ErrorMessage().render(options={"message": "Informações incorretas"})

    def render_content(self) -> None:
        pass

    def interaction(self, state: ScreenState | None = None) -> Order:
        id: UUID = uuid4()
        investor_id: UUID = uuid4()
        asset_id: UUID = uuid4()
        side: OrderSide = self._get_side()
        execution_type: ExecutionType = ExecutionType.MARKET
        status: OrderStatus = OrderStatus.PENDING

        quantity: int = 100
        executed: int = 0
        limit_price: Decimal = Decimal(150.0)
        stop_price: Decimal = Decimal(150.0)
        time_in_force: TimeInForce = TimeInForce.DAY

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
