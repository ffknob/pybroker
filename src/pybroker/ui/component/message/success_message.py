from dataclasses import dataclass
from rich.console import Console
from rich.text import Text

from pybroker.constant import icon
from pybroker.ui.component import BaseUIComponent, BaseUIComponentOptions

console = Console()


@dataclass(frozen=True)
class SuccessMessageOptions(BaseUIComponentOptions):
    message: str


class SuccessMessage(BaseUIComponent[SuccessMessageOptions, None]):
    def __init__(self, options: SuccessMessageOptions) -> None:
        super().__init__(options)

    def render(self) -> None:
        message: str = self.options.message

        console.print(Text().append(f"{icon.SUCCESS} {message}", style="green"))
