from pydantic import EmailStr, SecretStr

from pybroker.enums.usuario import PerfilUsuario
from pybroker.schema.base import BaseSchema


class Usuario(BaseSchema):
    nome: str
    email: EmailStr
    password: SecretStr
    perfil: PerfilUsuario
    ativo: bool
