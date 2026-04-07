from rich.prompt import Prompt

from pybroker.ui.screen import ScreenState
from pybroker.ui.screen import BaseScreen
from pybroker.model import MenuOption
from pybroker.constant.colors import TEXT_INPUT


class MenuScreen(BaseScreen[None, MenuOption]):
    def __init__(self, menu_options: list[MenuOption] = []):
        super().__init__()

        self.menu_options: list[MenuOption] = menu_options
        self.menu: dict[int, MenuOption] = {}

    def render_menu(self) -> None:
        sorted_menu_options = sorted(
            self.menu_options,
            key=lambda menu_option: menu_option.order
            if menu_option.order is not None
            else 0,
        )

        self.menu: dict[int, MenuOption] = {
            i: menu_option for i, menu_option in enumerate(sorted_menu_options, start=1)
        }

        for i, menu_option in self.menu.items():
            description: str = f"{menu_option.icon} {menu_option.description}"

            print(f"{i} - {description}")

    def get_user_input(self) -> int:
        selected_menu_option: int = 0

        while not selected_menu_option:
            try:
                selected_menu_option = int(
                    Prompt.ask(f"[{TEXT_INPUT}]🔢? [/{TEXT_INPUT}]")
                )

            except KeyError:
                print("Valor inválido")

        return selected_menu_option

    def execute(self, state: ScreenState | None = None) -> MenuOption:
        self.render_menu()

        selected_menu_option: int = 0

        while not selected_menu_option:
            selected_menu_option = self.get_user_input()

        return self.menu[selected_menu_option]
