from rich.prompt import Prompt

from pybroker.ui.screen import BaseScreen
from pybroker.model import MenuOption
from pybroker.constant.colors import TEXTO_INPUT


class MenuScreen(BaseScreen[list[MenuOption], MenuOption]):
    def __init__(self, menu_options: list[MenuOption] = []):
        super().__init__()

        self.menu_options: list[MenuOption] = menu_options

    def execute(self, state: None) -> MenuOption:
        opcoes_menu: list[MenuOption] = state
        opcoes_menu_ordenadas = sorted(
            opcoes_menu,
            key=lambda opcao_menu: opcao_menu.order
            if opcao_menu.order is not None
            else 0,
        )
        menu: dict[int, MenuOption] = {
            i: opcao_menu for i, opcao_menu in enumerate(opcoes_menu_ordenadas, start=1)
        }

        for i, opcao_menu in menu.items():
            descricao: str = f"{opcao_menu.icon} {opcao_menu.description}"

            print(f"{i} - {descricao}")

        item_menu_selecionado: int = 0

        while not item_menu_selecionado:
            try:
                item_menu_selecionado = int(
                    Prompt.ask(f"[{TEXTO_INPUT}]🔢? [/{TEXTO_INPUT}]")
                )

            except KeyError:
                print("Valor inválido")

        return menu[item_menu_selecionado]
