from dataclasses import dataclass
from typing import Generic, TypeVar, Any

from pybroker.ui.component.input import (
    AbstractInput,
)


@dataclass
class BaseInputOptions:
    label: str


SpecificInputOptions = TypeVar("SpecificInputOptions", bound=BaseInputOptions)
SpecificInputReturn = TypeVar("SpecificInputReturn", bound=Any)


class BaseInput(
    AbstractInput[SpecificInputOptions, SpecificInputReturn],
    Generic[SpecificInputOptions, SpecificInputReturn],
):
    pass
