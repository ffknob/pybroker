from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class BaseSchema(BaseModel):
    id: UUID
    criado_em: datetime
    atualizado_em: datetime
    excluido_em: datetime | None = None
