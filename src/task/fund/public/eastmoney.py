""" 天天基金网

"""
#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
from enum import Enum

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------
class EastMoneyIsLatest(Enum):
    """天天基金网 仅看最新日期"""
    """仅看最新日期 isLatest=1"""
    LATEST_ONLY = 1
    """全部 isLatest=0"""
    ALL = 0

class EastMoneyLX(Enum):
    """天天基金网 类型"""

    """全部"""
    ALL = 1
    """指数型"""
    INDEX_FUND = 8
    """股票型"""
    STOCK_FUND = 2
    """混合型"""
    MIX_FUND = 3
    """债券型"""
    BOND_FUND = 4
    """QDII"""
    QDII_FUND = 7
    """FOF"""
    FOF_FUND = 15

class EastMoneyIndexStockFeature(Enum):
    """天天基金网 指数型 跟踪标的类型"""
    """全部"""
    INDEX_STOCK_FEATURE_ALL = ""
    """沪深指数"""
    INDEX_STOCK_FEATURE_SHANGHAI_SHENZHEN = "053"
    """行业主题"""
    INDEX_STOCK_FEATURE_TOPIC = "054"
    """大盘指数"""
    INDEX_STOCK_FEATURE_MARKET = "01"
    """中小盘指数"""
    INDEX_STOCK_FEATURE_MID_SMALL_CAP = "02,03"
    """股票指数"""
    INDEX_STOCK_FEATURE_STOCK = "001"
    """债券指数"""
    INDEX_STOCK_FEATURE_BOND = "003"

class EastMoneyIndexStockTracking(Enum):
    """天天基金网 指数型 跟踪方式类型"""
    """全部"""
    INDEX_STOCK_TRACK_ALL = ""
    """被动指数型"""
    INDEX_STOCK_TRACK_PASSIVE= "051"
    """增强指数型"""
    INDEX_STOCK_TRACK_ENHANCE = "052"


class EastMoneyBondFeature(Enum):
    """天天基金网 债券类型"""
    """长期纯债"""
    BOND_FEATURE_LONG = "041|"
    """短期纯债"""
    BOND_FEATURE_SHORT = "042|"
    """混合债基"""
    BOND_FEATURE_MIX = "043|"
    """定期开放债券"""
    BOND_FEATURE_LIMITED_OPEN = "008|"
    """可转债"""
    BOND_FEATURE_CONVERTIBLE = "045|"

class EastMoneyQDIIFeature(Enum):
    """天天基金网 QDII类型"""
    """全部"""
    QDII_FEATURE_ALL = ""
    """全球股票"""
    QDII_FEATURE_GLOBAL_STOCK = "311"
    """亚太股票"""
    QDII_FEATURE_ASIA_STOCK = "312"
    """大中华区"""
    QDII_FEATURE_GCG_STOCK = "313"
    """美国股票"""
    QDII_FEATURE_US_STOCK = "317"
    """股债混合"""
    QDII_FEATURE_MIX = "320"
    """债券"""
    QDII_FEATURE_BOND = "330"
    """商品"""
    QDII_FEATURE_COMMODITY = "340"
#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------

if __name__ == '__main__':
    fetch_public_fund_task = FetchPublicFundTask()
    fetch_public_fund_task.run()
