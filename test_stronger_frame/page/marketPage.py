# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/1/11 19:59
@File     :marketPage.py
-------------------------------
"""
from time import sleep

from selenium.webdriver.common.by import By

from test_stronger_frame.BaseFunctions import BasicFunction
from test_stronger_frame.page.manageStockPage import ManageStockPage
from test_stronger_frame.page.marketSearchPage import MarketSearchPage
from test_stronger_frame.StrongerFrameLogger import CustomLogger

logger = CustomLogger.onelogger()

class MarketPage(BasicFunction):

    def stocktList(self, flag: str = "true"):
        sleep(3)
        #所有自选股的股票代码
        logger.info("在股票行情页中返回所有自选股名字或代码")
        return_list = self.yaml_steps('../page/marketpage.yaml', flag=flag)["stocktList"]
        sleep(2)
        self.find_and_click(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/tab_name" and @text="雪球"]')

        return return_list


    def goto_manageStock(self):
        logger.info("从股票行情页前往股票管理页")
        self.yaml_steps('../page/marketpage.yaml')
        return ManageStockPage(self.driver)

    def goto_marketSearch(self):

        logger.info("从股票行情页前往股票搜索页")
        self.yaml_steps('../page/marketpage.yaml')

        return MarketSearchPage(self.driver)
