from dataclasses import dataclass
from rich.console import Console
from rich.text import Text

from pybroker.constant import icon
from pybroker.ui.component import BaseUIComponent, BaseUIComponentOptions

console = Console()


@dataclass(frozen=True)
class ErrorMessageOptions(BaseUIComponentOptions):
    message: str


class ErrorMessage(BaseUIComponent[ErrorMessageOptions, None]):
    def __init__(self, options: ErrorMessageOptions) -> None:
        super().__init__(options)

    def render(self) -> None:
        message: str = self.options.message

        console.print(Text().append(f"{icon.ERROR} {message}", style="red"))
