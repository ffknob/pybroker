from dataclasses import dataclass

from rich.prompt import Prompt

from pybroker.ui.component.input import BaseInput, BaseInputOptions
from pybroker.ui.component.message import ErrorMessage, ErrorMessageOptions
from pybroker.constant import style, text, icon


@dataclass(frozen=True)
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
            input: str = Prompt.ask(
                f"[{style.TEXT_INPUT}]{icon.NUMBER} {label}[/{style.TEXT_INPUT}]"
            )

            try:
                return int(input)

            except ValueError:
                ErrorMessage(
                    ErrorMessageOptions(message=text.MESSAGE_INVALID_VALUE)
                ).render()
