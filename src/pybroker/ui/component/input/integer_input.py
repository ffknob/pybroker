from dataclasses import dataclass

from rich.prompt import Prompt

from pybroker.ui.component.input import BaseInput, BaseInputOptions
from pybroker.ui.component import ErrorMessage
from pybroker.constant.style import TEXT_INPUT
from pybroker.constant.text import MESSAGE_INVALID_VALUE


@dataclass
class IntegerInputOptions(BaseInputOptions):
    pass


class IntegerInput(BaseInput[IntegerInputOptions, int]):
    # TODO: implementar validação
    def validate(self) -> bool:
        return True

    def render(self, options: IntegerInputOptions) -> int:
        label: str = options.label

        while True:
            input: str = Prompt.ask(f"🔢 [{TEXT_INPUT}]{label}[/{TEXT_INPUT}]")

            try:
                return int(input)

            except ValueError:
                ErrorMessage().render({"message": MESSAGE_INVALID_VALUE})
