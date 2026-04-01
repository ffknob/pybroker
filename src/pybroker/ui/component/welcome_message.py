from pybroker.ui.component import BaseUIComponent

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


class WelcomeMessage(BaseUIComponent[None, None]):
    def __init__(self):
        super().__init__()

    def _title(self) -> Text:
        return (
            Text()
            .append(
                "  ██████╗ ██╗   ██╗██████╗ ██████╗  ██████╗ ██╗  ██╗███████╗██████╗\n",
                style="bold bright_yellow",
            )
            .append(
                "  ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝██╔══██╗\n",
                style="bold bright_yellow",
            )
            .append(
                "  ██████╔╝ ╚████╔╝ ██████╔╝██████╔╝██║   ██║█████╔╝ █████╗  ██████╔╝\n",
                style="bold red",
            )
            .append(
                "  ██╔═══╝   ╚██╔╝  ██╔══██╗██╔══██╗██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗\n",
                style="bold red",
            )
            .append(
                "  ██║        ██║   ██████╔╝██║  ██║╚██████╔╝██║  ██╗███████╗██║  ██║\n",
                style="bold green",
            )
            .append(
                "  ╚═╝        ╚═╝   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\n",
                style="bold green",
            )
        )

    def _tagline(self) -> Text:
        return (
            Text()
            .append("📈  📊 Bem-vindo ao ", style="bold white")
            .append("PyBroker", style="bold bright_green")
            .append(" — sua solução para negociar ações via terminal.\n", style="white")
            .append(
                "• Cotações em tempo real  • Ordens automatizadas  • Análise de portfólio\n",
                style="bright_white",
            )
            .append("Informe suas credenciais para começar a negociar. ", style="white")
        )

    def _panel(self) -> Panel:
        title: Text = self._title()
        tagline: Text = self._tagline()

        panel_content = Text.assemble(title, "\n", tagline)

        return Panel.fit(
            panel_content,
            border_style="bright_blue",
            padding=(1, 4),
        )

    def render(self, options: None = None) -> None:
        panel: Panel = self._panel()

        console.print(panel)

        console.print("")
