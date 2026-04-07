from pybroker.enums.base import BaseEnum


class TimeInForce(BaseEnum):
    DAY = "day"
    GTC = "gtc"  # Good Till Cancelled
