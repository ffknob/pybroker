from typing import Generic

from rich.prompt import Prompt

from pybroker.ui.screen.abstract_screen import ScreenState, ScreenReturn
from pybroker.ui.screen.base_screen import BaseScreen
from pybroker.ui.component import ErrorMessage
from pybroker.constant.style import TEXT_INPUT
from pybroker.constant.text import MESSAGE_INVALID_VALUE


class FormScreen(
    BaseScreen[ScreenState, ScreenReturn], Generic[ScreenState, ScreenReturn]
):
    def __init__(self, title: str | None = None):
        super().__init__(title)

    def select(self, label: str, options: list[str]) -> str:
        return Prompt.ask(
            prompt=f"[{TEXT_INPUT}]📧 {label} [/{TEXT_INPUT}]",
            choices=options,
            show_choices=True,
        )

    def text_input(self, label: str) -> str:
        return Prompt.ask(f"🔤 {label}")

    def integer_input(self, label: str) -> int:
        while True:
            input: str = Prompt.ask(f"🔢 {label}")

            try:
                return int(input)

            except ValueError:
                ErrorMessage().render({"message": MESSAGE_INVALID_VALUE})

    def float_input(self, label: str) -> float:
        while True:
            input: str = Prompt.ask(f"🔢 {label}")

            try:
                return float(input)

            except ValueError:
                ErrorMessage().render({"message": MESSAGE_INVALID_VALUE})
