from typing import Generic

from pybroker.ui.screen.abstract_screen import ScreenState, ScreenReturn
from pybroker.ui.screen.base_screen import BaseScreen


class FormScreen(
    BaseScreen[ScreenState, ScreenReturn], Generic[ScreenState, ScreenReturn]
):
    def __init__(self, title: str | None = None):
        super().__init__(title)
