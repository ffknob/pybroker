import csv
import os
from typing import Any
from uuid import UUID

from pybroker.repository import AbstractOrderRepository
from pybroker.schema import Order

ORDERS: dict[UUID, Order] = {}

CSV_FIELDS = [
    "id",
    "investor_id",
    "asset_id",
    "ticker",
    "side",
    "execution_type",
    "time_in_force",
    "status",
    "quantity",
    "executed_quantity",
    "limit_price",
    "stop_price",
    "trailing_amount",
    "average_executed_price",
    "created_at",
    "updated_at",
    "deleted_at",
]


class CsvOrderRepository(AbstractOrderRepository):
    def __init__(self, file: str):
        self.file = file

    async def load(self) -> None:
        if not os.path.exists(self.file):
            return

        with open(self.file, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                normalized = {k: (v if v != "" else None) for k, v in row.items()}
                order = Order.model_validate(normalized)
                ORDERS[order.id] = order

    async def flush(self) -> None:
        with open(self.file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
            writer.writeheader()

            for order in ORDERS.values():
                writer.writerow(order.model_dump())

    async def get(self, id: UUID) -> Order | None:
        return ORDERS[id]

    async def all(self) -> list[Order]:
        return list(ORDERS.values())

    async def create(self, item: Order) -> Order:
        ORDERS[item.id] = item

        await self.flush()

        return item

    async def update(self, item: Order) -> Order:
        if item.id in ORDERS.keys():
            ORDERS[item.id] = item

        else:
            raise KeyError

        await self.flush()

        return item

    async def delete(self, item: Order) -> Order:
        if item.id in ORDERS.keys():
            del ORDERS[item.id]

        else:
            raise KeyError

        await self.flush()

        return item

    async def delete_by_id(self, id: UUID) -> Order:
        item: Order | None = None
        if id in ORDERS.keys():
            item = ORDERS[id]
            del ORDERS[id]

        else:
            raise KeyError

        await self.flush()

        return item

    async def find(self, property: str, value: Any) -> list[Order] | None:
        pass

    async def find_one(self, property: str, value: Any) -> Order | None:
        pass

    async def find_by_id(self, id: UUID) -> Order | None:
        pass

    async def exists(self, id: UUID) -> bool:
        return id in ORDERS.keys()
