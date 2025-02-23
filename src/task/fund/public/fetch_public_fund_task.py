''' 基金

'''
#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
import contextlib
import requests
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task import GeneralTask
from config import EnvConfig
from model.stock.db.timescaledb import PublicFundRealTime
import STPyV8

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------
# timescaledb链接字符串
_timescaledb_conn_str = EnvConfig.timescaledb_url

# 所有基金列表 http://fund.eastmoney.com/fund.html
_funds_list_url = 'http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?page=1,&onlySale=0'
_funds_realtime_list_url = 'https://www.dayfund.cn/prevalue.html'
_request_header = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/78.0.3904.108 Safari/537.36'}

engine = create_engine(
    _timescaledb_conn_str,
    echo=True,  # 是不是要把所执行的SQL打印出来，一般用于调试
    pool_size=4,  # 连接池大小
    max_overflow=0,  # 连接池最大的大小
    pool_recycle=6000,  # 多久时间主动回收连接，见下注释
    pool_pre_ping=True  # 事先ping确定连接是否存活
)
Session = sessionmaker(bind=engine)
#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------
class FetchPublicFundTask(GeneralTask):

    def __init__(self):
        super().__init__('FetchPublicFundTask')

    def run(self):
        fetch_url = _funds_list_url
        optime = datetime.now()
        page = requests.get(fetch_url, headers=_request_header)
        text = page.text
        records = []
        with STPyV8.JSContext() as ctxt:
            ctxt.eval(text)
            vars = ctxt.locals
            db = vars.db
            print(f'datas length = {len(db.datas)}, record={db.record}')
            for record in db.datas:
                records.append(str(record).split(','))

        #存入数据库
        for record in records:
            print(record)
            entity = PublicFundRealTime()
            # 例子
            # ["000011","华夏大盘精选混合A","HXDPJXHHA","15.56","22.816","15.273","22.529","0.287","1.88","限大额","开放赎回","","1","0","13","","1","0.15%","0.15%","1","1.50%"],
            # 数据收集时间
            entity.optime = optime
            # 公募基金代号
            entity.public_fund_symbol = record[0]
            # 基金简称
            entity.public_fund_name = record[1]
            # 基金简称拼音
            entity.public_fund_name_pinyin = record[2]
            # 最新单位净值
            entity.latest_nav_text = record[3]
            # 最新单位净值
            entity.latest_nav = get_float(record[3])
            # 最新累计净值
            entity.latest_cumulative_nav_text = record[4]
            # 最新单位净值
            entity.latest_cumulative_nav = get_float(record[4])
            # 历史单位净值
            entity.historical_nav_text = record[5]
            # 历史单位净值
            entity.historical_nav = get_float(record[5])
            # 历史累计净值
            entity.historical_cumulative_nav_text = record[6]
            # 历史累计净值
            entity.historical_cumulative_nav = get_float(record[6])
            # 日增长值
            entity.daily_growth_value_text = record[7]
            # 日增长值
            entity.daily_growth_value = get_float(record[7])
            # 日增长率
            entity.daily_growth_rate_text = record[8]
            # 日增长率
            entity.daily_growth_rate = get_float(record[8])
            # 申购状态
            entity.subscription_status = record[9]
            # 赎回状态
            entity.redemption_status = record[10]
            with get_session() as s:
                s.add(entity)

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------
@contextlib.contextmanager
def get_session():
    s = Session()
    try:
        yield s
        s.commit()
    except Exception as e:
        s.rollback()
        raise e
    finally:
        s.close()

def get_float(text) -> float | None:
    try:
        f = float(text)
        return f
    except ValueError:
        print(f"无法将 '{text}' 转换为浮点数")
        return None

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------

if __name__ == '__main__':
    fetch_public_fund_task = FetchPublicFundTask()
    fetch_public_fund_task.run()
