# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/1/11 20:00
@File     :manageStockPage.py
-------------------------------
"""
from test_stronger_frame.BaseFunctions import BasicFunction
from test_stronger_frame.StrongerFrameLogger import CustomLogger

logger = CustomLogger.onelogger()

class ManageStockPage(BasicFunction):
    def deleteStock(self, send_code, send_name: str = "", flag: str = "true"):
        from test_frame.page.market import MarketPage

        logger.info("在股票管理页中删除所选的股票")
        self.yaml_steps('../page/manageStockPage.yaml', send_code=send_code, send_name=send_name, flag=flag)
        return MarketPage(self.driver)