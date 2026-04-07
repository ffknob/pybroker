from decimal import Decimal

from pybroker.enums.asset_type import AssetType
from pybroker.schema.base import BaseSchema


class Asset(BaseSchema):
    ticker: str
    name: str
    type: AssetType
    exchange: str
    currency: str
    current_price: Decimal
    day_change: Decimal
    day_volume: Decimal
    active: bool
