from datetime import datetime
from decimal import Decimal
from uuid import UUID, uuid4

from pybroker.constant.text import REGISTER_ORDER_SCREEN_TITLE
from pybroker.ui.screen.form_screen import FormScreen
from pybroker.enums import OrderSide, ExecutionType, OrderStatus, TimeInForce
from pybroker.schema import User, Order


class RegisterOrderScreen(FormScreen[User, Order]):
    def __init__(self):
        super().__init__(REGISTER_ORDER_SCREEN_TITLE)

    def _get_side(self) -> OrderSide:
        return OrderSide(self.select(label="Side", options=OrderSide.values()))

    def _get_quantity(self) -> int:
        return self.integer_input(label="Quantity")

    def _get_limit_price(self) -> float:
        return self.float_input(label="Limit price")

    def render_content(self) -> None:
        pass

    def interaction(self, state: User | None = None) -> Order:
        id: UUID = uuid4()
        investor_id: UUID = uuid4()
        asset_id: UUID = uuid4()
        side: OrderSide = self._get_side()
        execution_type: ExecutionType = ExecutionType.MARKET
        status: OrderStatus = OrderStatus.PENDING

        quantity: int = self._get_quantity()
        executed: int = 0
        limit_price: Decimal = Decimal(self._get_limit_price())
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
