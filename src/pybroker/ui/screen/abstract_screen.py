from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any

ScreenOptions = TypeVar("ScreenOptions", bound=Any | None)
ScreenReturn = TypeVar("ScreenReturn", bound=Any | None)


class AbstractScreen(ABC, Generic[ScreenOptions, ScreenReturn]):
    @abstractmethod
    def execute(self, options: ScreenOptions) -> ScreenReturn:
        pass
