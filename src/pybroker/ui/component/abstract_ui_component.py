from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any

ComponentOptions = TypeVar("ComponentOptions", bound=Any)
ComponentReturn = TypeVar("ComponentReturn", bound=Any)


class AbstractUIComponent(ABC, Generic[ComponentOptions, ComponentReturn]):
    def __init__(self, options: ComponentOptions):
        self.options = options

    @abstractmethod
    def render(self) -> ComponentReturn:
        pass
