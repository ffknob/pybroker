from decimal import Decimal
from typing import Self
from uuid import UUID

from pydantic import model_validator

from pybroker.enums.order_status import OrderStatus
from pybroker.enums.execution_type import ExecutionType
from pybroker.enums.order_type import OrderType
from pybroker.schema.base import BaseSchema


class Order(BaseSchema):
    investor_id: UUID
    asset_id: UUID
    type: OrderType
    execution_type: ExecutionType
    status: OrderStatus
    quantity: int
    executed_quantity: int
    limit_price: Decimal | None = None
    stop_price: Decimal | None = None
    average_executed_price: Decimal | None = None

    @model_validator(mode="after")
    def validate_prices(self) -> Self:
        if self.execution_type in (ExecutionType.LIMIT, ExecutionType.STOP_LIMIT):
            if self.limit_price is None:
                raise ValueError("limit_price is required for limit orders")
        if self.execution_type in (ExecutionType.STOP, ExecutionType.STOP_LIMIT):
            if self.stop_price is None:
                raise ValueError("stop_price is required for stop orders")
        return self
