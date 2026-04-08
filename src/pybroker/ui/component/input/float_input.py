from dataclasses import dataclass

from rich.prompt import Prompt

from pybroker.ui.component.input import BaseInput, BaseInputOptions
from pybroker.ui.component import ErrorMessage
from pybroker.constant.style import TEXT_INPUT
from pybroker.constant.text import MESSAGE_INVALID_VALUE


@dataclass
class FloatInputOptions(BaseInputOptions):
    pass


class FloatInput(BaseInput[FloatInputOptions, float]):
    # TODO: implementar validação
    def validate(self) -> bool:
        return True

    def render(self, options: FloatInputOptions) -> float:
        label: str = options.label

        while True:
            input: str = Prompt.ask(f"[{TEXT_INPUT}]🔢 {label}[/{TEXT_INPUT}]")

            try:
                return float(input)

            except ValueError:
                ErrorMessage().render({"message": MESSAGE_INVALID_VALUE})
