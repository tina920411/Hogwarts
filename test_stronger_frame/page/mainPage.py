# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/1/11 19:59
@File     :mainPage.py
-------------------------------
"""
from test_stronger_frame.BaseFunctions import BasicFunction
from test_stronger_frame.page.homeSearchPage import HomeSearchPage
from test_stronger_frame.page.marketPage import MarketPage
from test_stronger_frame.StrongerFrameLogger import CustomLogger

logger = CustomLogger.onelogger()

class MainPage(BasicFunction):
    def goto_market(self):
        #self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/tab_name" and @text="行情"]')
        logger.info("从Main页面前往股市行情页")
        self.yaml_steps('../page/mainpage.yaml')

        return MarketPage(self.driver)

    def goto_search(self):
        logger.info("从Main页面前往搜索页")
        self.yaml_steps('../page/mainpage.yaml')

        return HomeSearchPage(self.driver)
