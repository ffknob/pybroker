from enum import Enum


class StatusOrdem(str, Enum):
    PENDENTE = "pendente"
    PARCIALMENTE_EXECUTADA = "parcialmente_executada"
    EXECUTADA = "executada"
    CANCELADA = "cancelada"
    EXPIRADA = "expirada"
