from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any

ComponentOptions = TypeVar("ComponentOptions", bound=dict | None)
ComponentReturn = TypeVar("ComponentReturn", bound=Any)


class AbstractUIComponent(ABC, Generic[ComponentOptions, ComponentReturn]):
    @abstractmethod
    def render(self, options: ComponentOptions) -> ComponentReturn:
        pass
