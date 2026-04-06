from rich.prompt import Prompt

from pybroker.ui.screen import BaseScreen
from pybroker.ui.component import WelcomeMessage
from pybroker.model import Credentials


class LoginScreen(BaseScreen[None, Credentials]):
    def execute(self, state: None = None) -> Credentials:
        WelcomeMessage().render()

        username = Prompt.ask("[bold cyan]📧 E-mail[/bold cyan]")
        password = Prompt.ask("[bold cyan]🔐 Enter password[/bold cyan]", password=True)

        return Credentials(username=username, password=password)
