from dataclasses import dataclass
from typing import Generic, TypeVar, Any

from pybroker.ui.component.input import (
    AbstractInput,
)


@dataclass
class BaseInputOptions:
    label: str


GenericBaseInputOptions = TypeVar("GenericBaseInputOptions", bound=BaseInputOptions)
GenericBaseInputReturn = TypeVar("GenericBaseInputReturn", bound=Any)


class BaseInput(
    AbstractInput[GenericBaseInputOptions, GenericBaseInputReturn],
    Generic[GenericBaseInputOptions, GenericBaseInputReturn],
):
    def __init__(self, options: GenericBaseInputOptions):
        super().__init__(options)
