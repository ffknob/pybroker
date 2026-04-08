from dataclasses import dataclass

from rich.prompt import Prompt

from pybroker.ui.component.input import BaseInput, BaseInputOptions
from pybroker.constant.style import TEXT_INPUT
# from pybroker.constant.text import MESSAGE_INVALID_VALUE


@dataclass
class SelectInputOptions(BaseInputOptions):
    choices: list[str]


class SelectInput(BaseInput[SelectInputOptions, str]):
    # TODO: implementar validação
    def validate(self) -> bool:
        return True

    def render(self, options: SelectInputOptions) -> str:
        label: str = options.label
        choices: list[str] = options.choices

        return Prompt.ask(
            prompt=f"[{TEXT_INPUT}]📧 {label} [/{TEXT_INPUT}]",
            choices=choices,
            show_choices=True,
        )
