from enum import Enum


class TipoExecucao(str, Enum):
    MERCADO = "mercado"
    LIMITADA = "limitada"
    STOP = "stop"
    STOP_LIMITADA = "stop_limitada"
