from typing import Any, Callable
from pydantic import BaseModel


class MenuOption(BaseModel):
    order: int | None
    icon: str
    name: str
    description: str
    action: Callable[[Any], Any] | Callable[[], Any]
