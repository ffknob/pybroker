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
    def __init__(self, options: IntegerInputOptions):
        super().__init__(options)

    # TODO: implementar validação
    def validate(self) -> bool:
        return True

    def render(self) -> int:
        label: str = self.options.label

        while True:
            input: str = Prompt.ask(f"🔢 [{TEXT_INPUT}]{label}[/{TEXT_INPUT}]")

            try:
                return int(input)

            except ValueError:
                ErrorMessage().render({"message": MESSAGE_INVALID_VALUE})
