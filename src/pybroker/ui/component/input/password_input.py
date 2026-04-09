from dataclasses import dataclass

from rich.prompt import Prompt

from pybroker.ui.component.input import BaseInput, BaseInputOptions
from pybroker.constant.style import TEXT_INPUT


@dataclass
class PasswordInputOptions(BaseInputOptions):
    pass


class PasswordInput(BaseInput[PasswordInputOptions, str]):
    def __init__(self, options: PasswordInputOptions):
        super().__init__(options)

    # TODO: implementar validação
    def validate(self) -> bool:
        return True

    def render(self) -> str:
        label: str = self.options.label

        return Prompt.ask(f"🔐 [{TEXT_INPUT}]{label}[/{TEXT_INPUT}]", password=True)
