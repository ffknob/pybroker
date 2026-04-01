from decimal import Decimal

from pybroker.enums.tipo_ativo import TipoAtivo
from pybroker.schema.base import BaseSchema


class Ativo(BaseSchema):
    ticker: str
    nome: str
    tipo: TipoAtivo
    bolsa: str
    moeda: str
    preco_atual: Decimal
    variacao_dia: Decimal
    volume_dia: Decimal
    ativo: bool
