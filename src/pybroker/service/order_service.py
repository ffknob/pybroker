from pybroker.service import AbstractOrderService
from pybroker.repository import AbstractOrderRepository
from pybroker.schema import Order


class OrderService(AbstractOrderService):
    def __init__(self, repository: AbstractOrderRepository):
        self.repository = repository

    async def list(self) -> list[Order]:
        return await self.repository.all()

    async def register(self, order: Order) -> Order:
        return await self.repository.create(order)

    async def update(self, order: Order) -> Order:
        return await self.repository.update(order)

    async def cancel(self, order: Order) -> Order:
        return await self.repository.delete(order)
