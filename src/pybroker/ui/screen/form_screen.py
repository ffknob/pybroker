from dataclasses import dataclass
from typing import TypeVar, Generic

from pybroker.ui.screen import ScreenReturn, BaseScreen, BaseScreenState


@dataclass
class FormScreenState(BaseScreenState):
    pass


GenericFormScreenState = TypeVar("GenericFormScreenState", bound=FormScreenState)


class FormScreen(
    BaseScreen[GenericFormScreenState, ScreenReturn],
    Generic[GenericFormScreenState, ScreenReturn],
):
    def __init__(
        self, title: str | None = None, state: GenericFormScreenState | None = None
    ):
        super().__init__(title, state)
