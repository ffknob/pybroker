from dataclasses import dataclass
from typing import TypeVar, Generic

from pybroker.ui.screen import ScreenReturn, BaseScreen, BaseScreenState


@dataclass(frozen=True)
class FormScreenState(BaseScreenState):
    pass


GenericFormScreenState = TypeVar("GenericFormScreenState", bound=FormScreenState)


class FormScreen(
    BaseScreen[GenericFormScreenState, ScreenReturn],
    Generic[GenericFormScreenState, ScreenReturn],
):
    def __init__(self, state: GenericFormScreenState):
        super().__init__(state)
