from abc import ABC, abstractmethod

from pybroker.schema import Order


class AbstractOrderService(ABC):
    @abstractmethod
    async def list(self) -> list[Order]:
        pass

    @abstractmethod
    async def register(self, order: Order) -> Order:
        pass

    @abstractmethod
    async def update(self, order: Order) -> Order:
        pass

    @abstractmethod
    async def cancel(self, order: Order) -> Order:
        pass
