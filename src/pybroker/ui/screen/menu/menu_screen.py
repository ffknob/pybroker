from dataclasses import dataclass

from pybroker.ui.screen.base_screen import BaseScreen, BaseScreenState
from pybroker.ui.component.input import IntegerInput, IntegerInputOptions
from pybroker.model import MenuOption


@dataclass(frozen=True)
class MenuScreenState(BaseScreenState):
    options: list[MenuOption]


class MenuScreen(BaseScreen[MenuScreenState, MenuOption]):
    def __init__(self, state: MenuScreenState):
        super().__init__(state)

        self.menu_options: list[MenuOption] = self.state.options
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

        print("\n")

    def _get_selected_menu_option(self) -> int:
        selected_menu_option: int = 0

        while not selected_menu_option:
            try:
                selected_menu_option = IntegerInput(
                    IntegerInputOptions(label="?")
                ).render()

            except KeyError:
                print("Valor inválido")

        return selected_menu_option

    def render_content(self) -> None:
        self.render_menu()

    def interaction(
        self,
    ) -> MenuOption:
        selected_menu_option: int = 0

        while not selected_menu_option:
            selected_menu_option = self._get_selected_menu_option()

        return self.menu[selected_menu_option]
