from dataclasses import dataclass

from rich.prompt import Prompt

from pybroker.ui.component.input import BaseInput, BaseInputOptions
from pybroker.constant import style, icon


@dataclass(frozen=True)
class SelectInputOptions(BaseInputOptions):
    choices: list[str]


class SelectInput(BaseInput[SelectInputOptions, str]):
    def __init__(self, options: SelectInputOptions):
        super().__init__(options)

    # TODO: implementar validação
    def validate(self) -> bool:
        return True

    def render(self) -> str:
        label: str = self.options.label
        choices: list[str] = self.options.choices

        return Prompt.ask(
            prompt=f"[{style.TEXT_INPUT}]{icon.SELECT} {label} [/{style.TEXT_INPUT}]",
            choices=choices,
            show_choices=True,
        )
