from abc import abstractmethod
from typing import TypeVar, Any

from pybroker.ui.component import AbstractUIComponent

InputOptions = TypeVar("InputOptions", bound=Any)
InputReturn = TypeVar("InputReturn", bound=Any)


class AbstractInput(AbstractUIComponent[InputOptions, InputReturn]):
    @abstractmethod
    def validate(self) -> bool:
        pass

    @abstractmethod
    def render(self, options: InputOptions) -> InputReturn:
        pass
