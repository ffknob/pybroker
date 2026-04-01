from datetime import date
from uuid import UUID

from pydantic import field_validator

from pybroker.enums.investidor import TipoPessoa
from pybroker.schema.base import BaseSchema


class Investidor(BaseSchema):
    usuario_id: UUID
    nome_completo: str
    tipo_pessoa: TipoPessoa
    cpf_cnpj: str
    data_nascimento: date | None = None
    telefone: str
    endereco: str

    @field_validator("cpf_cnpj")
    @classmethod
    def validar_cpf_cnpj(cls, v: str) -> str:
        digits = "".join(c for c in v if c.isdigit())
        if len(digits) not in (11, 14):
            raise ValueError("CPF deve ter 11 dígitos e CNPJ 14")
        return v
