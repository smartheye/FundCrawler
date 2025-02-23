from datetime import datetime
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, Float, String, DateTime, PrimaryKeyConstraint
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class PublicFundRealTime(Base):
    """公募基金实时净值"""
    __tablename__ = 't_public_fund_real_time'

    optime = Column(DateTime, name='optime', default=datetime.now, comment='数据收集时间')
    public_fund_symbol = Column(String, name='public_fund_symbol', comment='公募基金代号')
    public_fund_name = Column(String, name='public_fund_name', comment='基金简称')
    public_fund_name_pinyin = Column(String, name='public_fund_name_pinyin', comment='基金简称拼音')
    latest_nav_text = Column(String, name='latest_nav_text', comment='最新单位净值(latest net asset value)')
    latest_nav = Column(Float, name='latest_nav', comment='最新单位净值(latest net asset value)')
    latest_cumulative_nav_text = Column(String, name='latest_cumulative_nav_text', comment='最新累计净值（latest cumulative net asset value)')
    latest_cumulative_nav = Column(Float, name='latest_cumulative_nav', comment='最新累计净值（latest cumulative net asset value)')
    historical_nav_text = Column(String, name='historical_nav_text', comment='历史单位净值（historical net asset value）')
    historical_nav = Column(Float, name='historical_nav', comment='历史单位净值（historical net asset value）')
    historical_cumulative_nav_text = Column(String, name='historical_cumulative_nav_text', comment='历史累计净值（historical cumulative net asset value）')
    historical_cumulative_nav = Column(Float, name='historical_cumulative_nav', comment='历史累计净值（historical cumulative net asset value）')
    daily_growth_value_text = Column(String, name='daily_growth_value_text', comment='日增长值')
    daily_growth_value = Column(Float, name='daily_growth_value', comment='日增长值')
    daily_growth_rate_text = Column(String, name='daily_growth_rate_text', comment='日增长率')
    daily_growth_rate = Column(Float, name='daily_growth_rate', comment='日增长率')
    subscription_status = Column(String, name='subscription_status', comment='申购状态')
    redemption_status = Column(String, name='redemption_status', comment='赎回状态')

    __table_args__ = (
        PrimaryKeyConstraint('optime', 'public_fund_symbol'),
        {
            'schema': 'public',
        },
    )