from decimal import Decimal
from typing import Self
from uuid import UUID

from pydantic import model_validator

from pybroker.enums.status_ordem import StatusOrdem
from pybroker.enums.tipo_execucao import TipoExecucao
from pybroker.enums.tipo_ordem import TipoOrdem
from pybroker.schema.base import BaseSchema


class Ordem(BaseSchema):
    investidor_id: UUID
    ativo_id: UUID
    tipo: TipoOrdem
    tipo_execucao: TipoExecucao
    status: StatusOrdem
    quantidade: int
    quantidade_executada: int
    preco_limite: Decimal | None = None
    preco_stop: Decimal | None = None
    preco_medio_executado: Decimal | None = None

    @model_validator(mode="after")
    def validar_precos(self) -> Self:
        if self.tipo_execucao in (TipoExecucao.LIMITADA, TipoExecucao.STOP_LIMITADA):
            if self.preco_limite is None:
                raise ValueError("preco_limite é obrigatório para ordens limitadas")
        if self.tipo_execucao in (TipoExecucao.STOP, TipoExecucao.STOP_LIMITADA):
            if self.preco_stop is None:
                raise ValueError("preco_stop é obrigatório para ordens stop")
        return self
