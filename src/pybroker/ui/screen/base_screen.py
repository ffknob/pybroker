from dataclasses import dataclass
from typing import TypeVar, Generic

from rich.console import Console
from rich.rule import Rule

from pybroker.ui.screen.abstract_screen import AbstractScreen, ScreenReturn
from pybroker.constant import style

console = Console()


@dataclass
class BaseScreenState:
    pass


GenericBaseScreenState = TypeVar("GenericBaseScreenState", bound=BaseScreenState)


class BaseScreen(
    AbstractScreen[GenericBaseScreenState, ScreenReturn],
    Generic[GenericBaseScreenState, ScreenReturn],
):
    def __init__(
        self, title: str | None = None, state: GenericBaseScreenState | None = None
    ):
        self.title: str | None = title
        self.state: GenericBaseScreenState | None = state

    def clear(self) -> None:
        print("\n\n")

    def render_title(self) -> None:
        if self.title:
            console.print(
                Rule(
                    title=f"[{style.TITLE_TEXT}]{self.title}[/{style.TITLE_TEXT}]",
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
