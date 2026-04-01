from decimal import Decimal
from uuid import UUID

from pydantic import computed_field

from pybroker.schema.base import BaseSchema


class PosicaoCarteira(BaseSchema):
    investidor_id: UUID
    ativo_id: UUID
    ticker: str
    quantidade: int
    preco_medio: Decimal
    preco_atual: Decimal

    @computed_field  # type: ignore[prop-decorator]
    @property
    def valor_investido(self) -> Decimal:
        return self.preco_medio * self.quantidade

    @computed_field  # type: ignore[prop-decorator]
    @property
    def valor_atual(self) -> Decimal:
        return self.preco_atual * self.quantidade

    @computed_field  # type: ignore[prop-decorator]
    @property
    def lucro_prejuizo(self) -> Decimal:
        return self.valor_atual - self.valor_investido

    @computed_field  # type: ignore[prop-decorator]
    @property
    def rentabilidade(self) -> Decimal:
        if self.valor_investido == 0:
            return Decimal("0")
        return (self.lucro_prejuizo / self.valor_investido * 100).quantize(Decimal("0.01"))


class Carteira(BaseSchema):
    investidor_id: UUID
    posicoes: list[PosicaoCarteira]
    saldo_disponivel: Decimal

    @computed_field  # type: ignore[prop-decorator]
    @property
    def valor_total(self) -> Decimal:
        return self.saldo_disponivel + sum(p.valor_atual for p in self.posicoes)
