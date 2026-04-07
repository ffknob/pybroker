from enum import Enum


class AssetType(str, Enum):
    STOCK = "stock"
    FII = "fii"
    ETF = "etf"
    FIXED_INCOME = "fixed_income"
    BDR = "bdr"
    OPTION = "option"
