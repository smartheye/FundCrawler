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
        js_text = page.text
        with STPyV8.JSContext() as ctxt:
            ctxt.eval(js_text)
            vars = ctxt.locals
            logger.info(vars.db.datas)
