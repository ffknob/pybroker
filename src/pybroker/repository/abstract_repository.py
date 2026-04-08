from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

Id = TypeVar("Id", bound=Any)
T = TypeVar("T", bound=Any)


class AbstractRepository(ABC, Generic[Id, T]):
    @abstractmethod
    async def get(self, id: Id) -> T | None:
        pass

    @abstractmethod
    async def all(self) -> list[T]:
        pass

    @abstractmethod
    async def create(self, item: T) -> T:
        pass

    @abstractmethod
    async def update(self, item: T) -> T:
        pass

    @abstractmethod
    async def delete(self, item: T) -> T:
        pass

    @abstractmethod
    async def delete_by_id(self, id: Id) -> T:
        pass

    @abstractmethod
    async def find(self, property: str, value: Any) -> list[T] | None:
        pass

    @abstractmethod
    async def find_one(self, property: str, value: Any) -> T | None:
        pass

    @abstractmethod
    async def find_by_id(self, id: Id) -> T | None:
        pass

    @abstractmethod
    async def exists(self, id: Id) -> bool:
        pass
