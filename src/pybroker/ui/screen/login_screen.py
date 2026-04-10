from dataclasses import dataclass

from pybroker.ui.screen import BaseScreen, BaseScreenState
from pybroker.ui.component import WelcomeMessage, WelcomeMessageOptions
from pybroker.ui.component.input import (
    EmailInput,
    EmailInputOptions,
    PasswordInput,
    PasswordInputOptions,
)
from pybroker.model import Credentials


@dataclass(frozen=True)
class LoginScreenState(BaseScreenState):
    pass


class LoginScreen(BaseScreen[LoginScreenState, Credentials]):
    def __init__(self, state: LoginScreenState):
        super().__init__(state)

    def render_content(self) -> None:
        WelcomeMessage(WelcomeMessageOptions()).render()

    def interaction(self) -> Credentials:
        username = EmailInput(EmailInputOptions(label="E-mail")).render()
        password = PasswordInput(PasswordInputOptions(label="Password")).render()

        return Credentials(username=username, password=password)
