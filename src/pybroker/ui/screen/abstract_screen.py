from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any

ScreenState = TypeVar("ScreenState", bound=Any)
ScreenReturn = TypeVar("ScreenReturn", bound=Any)


class AbstractScreen(ABC, Generic[ScreenState, ScreenReturn]):
    @abstractmethod
    def execute(self, state: ScreenState | None = None) -> ScreenReturn:
        pass
