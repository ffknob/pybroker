from pybroker.ui.screen import BaseScreen
from pybroker.ui.component import WelcomeMessage
from pybroker.model import Credentials


class LoginScreen(BaseScreen[None, Credentials]):
    def execute(self) -> Credentials:
        WelcomeMessage().render()

        username = input("E-mail: ")
        password = input("Password: ")

        return Credentials(username=username, password=password)
