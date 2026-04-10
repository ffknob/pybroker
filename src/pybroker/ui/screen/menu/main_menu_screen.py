from dataclasses import dataclass

from pybroker.ui.screen.menu import (
    MenuScreen,
    MenuScreenState,
)


@dataclass(frozen=True)
class MainMenuScreenState(MenuScreenState):
    pass


class MainMenuScreen(MenuScreen):
    def __init__(self, state: MainMenuScreenState):
        super().__init__(state)
