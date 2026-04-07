from pybroker.ui.screen import MenuScreen, ScreenState
from pybroker.model import MenuOption

MENU: list[MenuOption] = [
    MenuOption(
        order=1,
        name="REGISTRAR",
        description="Registrar ordem",
        icon="📝",
        action=lambda: print("Registrar ordem"),
    ),
    MenuOption(
        order=2,
        name="CONSULTAR",
        description="Consultar ordens",
        icon="🔍",
        action=lambda: print("Consultar ordens"),
    ),
    MenuOption(
        order=3,
        name="ALTERAR",
        description="Alterar ordem",
        icon="✏️",
        action=lambda: print("Alterar ordem"),
    ),
    MenuOption(
        order=4,
        name="CANCELAR",
        description="Cancelar ordem",
        icon="❌",
        action=lambda: print("Cancelar ordem"),
    ),
    MenuOption(
        order=9,
        name="SAIR",
        description="Sair",
        icon="🚪",
        action=lambda: exit(0),
    ),
]


class MainMenuScreen(MenuScreen):
    def __init__(self):
        super().__init__(MENU)

    def execute(self, state: ScreenState | None = None) -> MenuOption:
        return super().execute()
