from uuid import UUID
from datetime import datetime
from pydantic import SecretStr

from pybroker.enums.usuario import PerfilUsuario
from pybroker.provider.auth import AbstractAuthenticationProvider
from pybroker.model import Credentials
from pybroker.schema import Usuario


class UsernamePasswordAuthProvider(AbstractAuthenticationProvider):
    def authenticate(self, credentials: Credentials) -> bool:
        # TODO: recuperar usuário do repositório
        usuario: Usuario = Usuario(
            id=UUID("0230dc7b-6041-4805-a5e4-ed793d5a0062"),
            nome="Flávio Knob",
            email="ffknob@gmail.com",
            password=SecretStr("123456"),
            perfil=PerfilUsuario.CLIENTE,
            ativo=True,
            criado_em=datetime.fromisoformat("2024-06-01T00:00:00Z"),
            atualizado_em=datetime.fromisoformat("2024-06-01T00:00:00Z"),
        )

        return (
            credentials.username == usuario.email
            and SecretStr(credentials.password) == usuario.password
        )
