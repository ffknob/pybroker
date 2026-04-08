from uuid import UUID

from pybroker.repository import AbstractRepository
from pybroker.schema.order import Order


class AbstractOrderRepository(AbstractRepository[UUID, Order]):
    pass
