from pybroker.enums.base import BaseEnum


class OrderStatus(BaseEnum):
    PENDING = "pending"
    PARTIALLY_EXECUTED = "partially_executed"
    EXECUTED = "executed"
    CANCELLED = "cancelled"
    EXPIRED = "expired"
