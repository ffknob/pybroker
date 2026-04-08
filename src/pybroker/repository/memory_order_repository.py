from typing import Any
from uuid import UUID

from pybroker.repository import AbstractOrderRepository
from pybroker.schema import Order

ORDERS: dict[UUID, Order] = {}


class MemoryOrderRepository(AbstractOrderRepository):
    async def get(self, id: UUID) -> Order | None:
        return ORDERS[id]

    async def all(self) -> list[Order]:
        return list(ORDERS.values())

    async def create(self, item: Order) -> Order:
        ORDERS[item.id] = item

        return item

    async def update(self, item: Order) -> Order:
        if item.id in ORDERS.keys():
            ORDERS[item.id] = item

        else:
            raise KeyError

        return item

    async def delete(self, item: Order) -> Order:
        if item.id in ORDERS.keys():
            del ORDERS[item.id]

        else:
            raise KeyError

        return item

    async def delete_by_id(self, id: UUID) -> Order:
        item: Order | None = None
        if id in ORDERS.keys():
            item = ORDERS[id]
            del ORDERS[id]

        else:
            raise KeyError

        return item

    async def find(self, property: str, value: Any) -> list[Order] | None:
        pass

    async def find_one(self, property: str, value: Any) -> Order | None:
        pass

    async def find_by_id(self, id: UUID) -> Order | None:
        pass

    async def exists(self, id: UUID) -> bool:
        return id in ORDERS.keys()
