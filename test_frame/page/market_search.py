# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/1/10 15:40
@File     :market_search.py
-------------------------------
"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from test_frame.BaseFunctions import BasicFunction


class MarketSearch(BasicFunction):

    def search(self):
        self.find_and_send(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]', "alibaba")
        sleep(3)
        print("ok")
        return True