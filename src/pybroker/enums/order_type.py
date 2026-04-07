from enum import Enum


class OrderType(str, Enum):
    BUY = "buy"
    SELL = "sell"
