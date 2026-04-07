from pybroker.enums.base import BaseEnum


class AssetType(BaseEnum):
    STOCK = "stock"
    FII = "fii"
    ETF = "etf"
    FIXED_INCOME = "fixed_income"
    BDR = "bdr"
    OPTION = "option"
