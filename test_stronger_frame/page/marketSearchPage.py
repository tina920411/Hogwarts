# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/1/13 17:45
@File     :marketSearchPage.py
-------------------------------
"""
from test_stronger_frame.BaseFunctions import BasicFunction
from test_stronger_frame.StrongerFrameLogger import CustomLogger

logger = CustomLogger.onelogger()

class MarketSearchPage(BasicFunction):

    def marketSearch(self, send_code):

        logger.info("在股票搜索页中搜索股票")
        self.yaml_steps('../page/marketSearchPage.yaml', send_code=send_code)
        return True