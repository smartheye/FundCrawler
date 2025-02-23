# test_parse_js_variable.py
import logging
import pytest

import requests
import STPyV8

logger = logging.getLogger(__name__)

class TestParseJsVariable:

    def get_eastmoney_page(self) -> str:
        url = 'http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?page=1,&onlySale=0'
        page = requests.get(url, headers={
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/78.0.3904.108 Safari/537.36'})
        return page

    def test_get_eastmoney_page(self):
        # assert self.capital_case('semaphore') == 'Semaphore'
        page = self.get_eastmoney_page()
        #print(page)
        logger.info(page.text)
        # ["012959","平安盈悦稳进回报1年持有混合(FOF)A","PAYYWJHB1NCYHHFOFA","","","0.9317","0.9317","","","开放申购","开放赎回","","1","0","19557","","1","0.12%","0.12%","1","1.20%"]
        # "000011", 基金代码
        #  "华夏大盘精选混合A", 基金简称
        #  "HXDPJXHHA", 基金简称拼音
        #  "15.56", 最新净值（单位净值）
        #  "22.816", 最新净值（累计净值）
        #  "15.273", 历史净值（单位净值）
        #  "22.529", 历史净值（累计净值）
        #  "0.287", 日增长值
        #  "1.88", 日增长率
        #  "限大额", 申购状态
        #  "开放赎回", 赎回状态
        #  "",
        #  "1",
        #  "0",
        #  "13",
        #  "",
        #  "1",
        #  "0.15%",
        #  "0.15%",
        #  "1",
        #  "1.50%"
        # js_text = page.text
        # with STPyV8.JSContext() as ctxt:
        #     ctxt.eval(js_text)
        #     vars = ctxt.locals
        #     logger.info(vars.db.datas)
