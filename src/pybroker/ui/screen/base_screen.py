from dataclasses import dataclass
from typing import TypeVar, Generic

from rich.console import Console
from rich.rule import Rule

from pybroker.ui.screen.abstract_screen import AbstractScreen, ScreenReturn
from pybroker.constant import style

console = Console()


@dataclass(frozen=True)
class BaseScreenState:
    title: str
    icon: str
    show_title: bool


GenericBaseScreenState = TypeVar("GenericBaseScreenState", bound=BaseScreenState)


class BaseScreen(
    AbstractScreen[GenericBaseScreenState, ScreenReturn],
    Generic[GenericBaseScreenState, ScreenReturn],
):
    def __init__(self, state: GenericBaseScreenState):
        self.state: GenericBaseScreenState = state

    def clear(self) -> None:
        print("\n\n")

    def render_title(self) -> None:
        if self.state.title:
            console.print(
                Rule(
                    title=f"[{style.TITLE_TEXT}]{self.state.icon} {self.state.title}[/{style.TITLE_TEXT}]",
                    style=style.TITLE_BAR,
                    align="left",
                )
            )

            print("\n")

    def execute(self) -> ScreenReturn:
        self.clear()

        self.render_title()

        self.render_content()

        return self.interaction()
