from dataclasses import dataclass

from rich.prompt import Prompt

from pybroker.ui.component.input import BaseInput, BaseInputOptions
from pybroker.constant.style import TEXT_INPUT


@dataclass
class TextInputOptions(BaseInputOptions):
    pass


class TextInput(BaseInput[TextInputOptions, str]):
    # TODO: implementar validação
    def validate(self) -> bool:
        return True

    def render(self, options: TextInputOptions) -> str:
        label: str = options.label

        return Prompt.ask(f"🔤 [{TEXT_INPUT}]{label}[/{TEXT_INPUT}]")
