from pybroker.ui.screen import BaseScreen


class MenuScreen(BaseScreen[dict[int, str], int]):
    def execute(self, options: dict[int, str]) -> int:
        for opcao, descricao in options.items():
            print(f"{opcao} - {descricao}")

        opcao_selecionada: int = int(input("Opção desejada: "))

        return opcao_selecionada
