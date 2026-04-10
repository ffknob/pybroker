from dataclasses import dataclass

from rich.console import Console

from pybroker.ui.component.display import BaseDisplay, BaseDisplayOptions

console = Console()


@dataclass(frozen=True)
class KeyValueDisplayOptions(BaseDisplayOptions):
    key: str
    value: str
    key_style: str
    value_style: str


class KeyValueDisplay(BaseDisplay):
    def __init__(self, options: KeyValueDisplayOptions):
        super().__init__(options)

    def render(self) -> None:
        key: str = self.options.key
        value: str = self.options.value

        key_style: str = self.options.key_style
        value_style: str = self.options.value_style

        return console.print(
            f"[{key_style}]{key}[/{key_style}] [{value_style}]{value}[/{value_style}]"
        )
