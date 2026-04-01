from enum import Enum


class PerfilUsuario(str, Enum):
    ADMIN = "admin"
    OPERADOR = "operador"
    CLIENTE = "cliente"
