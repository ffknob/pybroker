from abc import abstractmethod
from typing import TypeVar, Any

from pybroker.ui.component import AbstractUIComponent

InputOptions = TypeVar("InputOptions", bound=Any)
InputReturn = TypeVar("InputReturn", bound=Any)


class AbstractInput(AbstractUIComponent[InputOptions, InputReturn]):
    def __init__(self, options: InputOptions):
        super().__init__(options)

    @abstractmethod
    def validate(self) -> bool:
        pass

    @abstractmethod
    def render(self) -> InputReturn:
        pass
