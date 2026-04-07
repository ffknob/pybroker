from decimal import Decimal
from uuid import UUID

from pydantic import computed_field

from pybroker.schema.base import BaseSchema


class PortfolioPosition(BaseSchema):
    investor_id: UUID
    asset_id: UUID
    ticker: str
    quantity: int
    average_price: Decimal
    current_price: Decimal

    @computed_field  # type: ignore[prop-decorator]
    @property
    def invested_value(self) -> Decimal:
        return self.average_price * self.quantity

    @computed_field  # type: ignore[prop-decorator]
    @property
    def current_value(self) -> Decimal:
        return self.current_price * self.quantity

    @computed_field  # type: ignore[prop-decorator]
    @property
    def profit_loss(self) -> Decimal:
        return self.current_value - self.invested_value

    @computed_field  # type: ignore[prop-decorator]
    @property
    def profitability(self) -> Decimal:
        if self.invested_value == 0:
            return Decimal("0")
        return (self.profit_loss / self.invested_value * 100).quantize(Decimal("0.01"))


class Portfolio(BaseSchema):
    investor_id: UUID
    positions: list[PortfolioPosition]
    available_balance: Decimal

    @computed_field  # type: ignore[prop-decorator]
    @property
    def total_value(self) -> Decimal:
        return self.available_balance + sum(p.current_value for p in self.positions)
