from dataclasses import dataclass
from typing import Generic, Any, TypeVar

from pybroker.ui.component import AbstractUIComponent


@dataclass(frozen=True)
class BaseUIComponentOptions:
    pass


GenericBaseUIComponentOptions = TypeVar(
    "GenericBaseUIComponentOptions", bound=BaseUIComponentOptions
)
GenericBaseUIComponentReturn = TypeVar("GenericBaseUIComponentReturn", bound=Any)


class BaseUIComponent(
    AbstractUIComponent[GenericBaseUIComponentOptions, GenericBaseUIComponentReturn],
    Generic[GenericBaseUIComponentOptions, GenericBaseUIComponentReturn],
):
    def __init__(self, options: GenericBaseUIComponentOptions):
        super().__init__(options)
