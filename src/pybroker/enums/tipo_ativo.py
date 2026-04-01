from enum import Enum


class TipoAtivo(str, Enum):
    ACAO = "acao"
    FII = "fii"
    ETF = "etf"
    RENDA_FIXA = "renda_fixa"
    BDR = "bdr"
    OPCAO = "opcao"
