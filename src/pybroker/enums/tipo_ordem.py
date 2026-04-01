from enum import Enum


class TipoOrdem(str, Enum):
    COMPRA = "compra"
    VENDA = "venda"
