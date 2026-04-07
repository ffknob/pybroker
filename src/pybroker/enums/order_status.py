from enum import Enum


class OrderStatus(str, Enum):
    PENDING = "pending"
    PARTIALLY_EXECUTED = "partially_executed"
    EXECUTED = "executed"
    CANCELLED = "cancelled"
    EXPIRED = "expired"
