from rich.console import Console
from rich.text import Text

from pybroker.ui.component import BaseUIComponent

console = Console()


class ErrorMessage(BaseUIComponent[dict[str, str], None]):
    def __init__(self):
        super().__init__()

    @staticmethod
    def render(options: dict[str, str]) -> None:
        message: str = options.get("message", "Erro desconhecido")

        console.print(Text().append(f"🚨 {message}", style="red"))
