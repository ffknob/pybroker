from typing import Any, Callable, Awaitable
from pydantic import BaseModel


class MenuOption(BaseModel):
    order: int | None
    icon: str
    name: str
    description: str
    action: Callable[..., Awaitable[Any]]
