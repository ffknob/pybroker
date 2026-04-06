from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any

ScreenOptions = TypeVar("ScreenOptions", bound=Any)
ScreenReturn = TypeVar("ScreenReturn", bound=Any)


class AbstractScreen(ABC, Generic[ScreenOptions, ScreenReturn]):
    @abstractmethod
    def execute(self, options: ScreenOptions) -> ScreenReturn:
        pass
