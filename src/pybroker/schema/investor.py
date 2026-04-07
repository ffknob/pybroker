from datetime import date
from uuid import UUID

from pydantic import field_validator

from pybroker.enums.person_type import PersonType
from pybroker.schema.base import BaseSchema


class Investor(BaseSchema):
    user_id: UUID
    full_name: str
    person_type: PersonType
    cpf_cnpj: str
    birth_date: date | None = None
    phone: str
    address: str

    @field_validator("cpf_cnpj")
    @classmethod
    def validate_cpf_cnpj(cls, v: str) -> str:
        digits = "".join(c for c in v if c.isdigit())
        if len(digits) not in (11, 14):
            raise ValueError("CPF must have 11 digits and CNPJ 14")
        return v
