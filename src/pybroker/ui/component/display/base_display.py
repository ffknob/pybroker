from dataclasses import dataclass
from typing import Generic, TypeVar, Any

from pybroker.ui.component.display import (
    AbstractDisplay,
)


@dataclass(frozen=True)
class BaseDisplayOptions:
    pass


GenericBaseDisplayOptions = TypeVar(
    "GenericBaseDisplayOptions", bound=BaseDisplayOptions
)
GenericBaseDisplayReturn = TypeVar("GenericBaseDisplayReturn", bound=Any)


class BaseDisplay(
    AbstractDisplay[GenericBaseDisplayOptions, GenericBaseDisplayReturn],
    Generic[GenericBaseDisplayOptions, GenericBaseDisplayReturn],
):
    def __init__(self, options: GenericBaseDisplayOptions):
        super().__init__(options)
