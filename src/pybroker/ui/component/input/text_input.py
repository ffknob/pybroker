from dataclasses import dataclass

from rich.prompt import Prompt

from pybroker.ui.component.input import BaseInput, BaseInputOptions
from pybroker.constant import style, icon


@dataclass(frozen=True)
class TextInputOptions(BaseInputOptions):
    pass


class TextInput(BaseInput[TextInputOptions, str]):
    def __init__(self, options: TextInputOptions):
        super().__init__(options)

    # TODO: implementar validação
    def validate(self) -> bool:
        return True

    def render(self) -> str:
        label: str = self.options.label

        return Prompt.ask(
            f"[{style.TEXT_INPUT}]{icon.TEXT} {label}[/{style.TEXT_INPUT}]"
        )
