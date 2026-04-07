from pybroker.constant.text import REGISTER_ORDER_SCREEN_TITLE
from pybroker.ui.screen import BaseScreen, ScreenState
from pybroker.schema import Order


class RegisterOrderScreen(BaseScreen[None, Order]):
    def __init__(self):
        super().__init__(REGISTER_ORDER_SCREEN_TITLE)

    def render(self) -> None:
        pass

    def execute(self, state: ScreenState | None = None) -> Order:
        pass
