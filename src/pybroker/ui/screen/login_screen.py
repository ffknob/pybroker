from rich.prompt import Prompt

from pybroker.ui.screen import BaseScreen
from pybroker.ui.component import WelcomeMessage
from pybroker.model import Credentials
from pybroker.constant.colors import TEXTO_INPUT


class LoginScreen(BaseScreen[None, Credentials]):
    def execute(self, state: None = None) -> Credentials:
        WelcomeMessage().render()

        username = Prompt.ask(f"[{TEXTO_INPUT}]📧 E-mail[/{TEXTO_INPUT}]")
        password = Prompt.ask(
            f"[{TEXTO_INPUT}]🔐 Enter password[/{TEXTO_INPUT}]", password=True
        )

        return Credentials(username=username, password=password)
