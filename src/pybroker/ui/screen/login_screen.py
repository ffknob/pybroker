from rich.prompt import Prompt

from pybroker.ui.screen import BaseScreen
from pybroker.ui.component import WelcomeMessage
from pybroker.model import Credentials
from pybroker.constant.style import TEXT_INPUT


class LoginScreen(BaseScreen[None, Credentials]):
    def render(self) -> None:
        WelcomeMessage().render()

    def execute(self, state: None = None) -> Credentials:
        username = Prompt.ask(f"[{TEXT_INPUT}]📧 E-mail[/{TEXT_INPUT}]")
        password = Prompt.ask(
            f"[{TEXT_INPUT}]🔐 Password[/{TEXT_INPUT}]", password=True
        )

        return Credentials(username=username, password=password)
