# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/1/7 20:29
@File     :main.py
-------------------------------
"""
from appium.webdriver.common.mobileby import MobileBy

from test_frame.BaseFunctions import BasicFunction
from test_frame.page.home_search import HomeSearchPage
from test_frame.page.market import MarketPage


class Main(BasicFunction):
    def goto_market(self):
        self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/tab_name" and @text="行情"]')
        return MarketPage(self.driver)

    def goto_search(self):

        return HomeSearchPage(self.driver)




