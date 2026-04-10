from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any

ScreenState = TypeVar("ScreenState", bound=Any)
ScreenReturn = TypeVar("ScreenReturn", bound=Any)


class AbstractScreen(ABC, Generic[ScreenState, ScreenReturn]):
    def __init__(self, state: ScreenState):
        self.state = state

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def render_content(self) -> None:
        pass

    @abstractmethod
    def interaction(self) -> ScreenReturn:
        pass

    @abstractmethod
    def execute(self) -> ScreenReturn:
        pass
