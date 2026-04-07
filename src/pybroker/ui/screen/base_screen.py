from rich.console import Console
from rich.rule import Rule

from pybroker.ui.screen import AbstractScreen, ScreenState, ScreenReturn
from pybroker.constant.style import TITLE_TEXT, TITLE_BAR

console = Console()


class BaseScreen(AbstractScreen[ScreenState, ScreenReturn]):
    def __init__(self, title: str | None = None):
        self.title: str | None = title

    def clear(self) -> None:
        print("\n\n")

    def render_title(self) -> None:
        if self.title:
            console.print(
                Rule(
                    title=f"[{TITLE_TEXT}]{self.title}[/{TITLE_TEXT}]",
                    style=TITLE_BAR,
                    align="left",
                )
            )

            print("\n")

    def render_screen(self) -> None:
        self.clear()

        self.render_title()

        self.render()
