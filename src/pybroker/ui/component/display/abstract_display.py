from abc import abstractmethod
from typing import TypeVar, Any

from pybroker.ui.component import AbstractUIComponent

DisplayOptions = TypeVar("DisplayOptions", bound=Any)
DisplayReturn = TypeVar("DisplayReturn", bound=Any)


class AbstractDisplay(AbstractUIComponent[DisplayOptions, DisplayReturn]):
    def __init__(self, options: DisplayOptions):
        super().__init__(options)

    @abstractmethod
    def render(self) -> DisplayReturn:
        pass
