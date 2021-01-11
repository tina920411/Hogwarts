# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/1/8 14:50
@File     :market.py
-------------------------------
"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from test_frame.BaseFunctions import BasicFunction
from test_frame.page.manageStock import ManageStockPage
from test_frame.page.market_search import MarketSearch


class MarketPage(BasicFunction):

    def stocktList(self, flag:bool=True):
        #所有自选股的股票代码
        sleep(3)
        stock_code_eles = self.finds(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/portfolio_stockCode"]')
        stock_code_list = []
        for index in range(len(stock_code_eles)):
            code = stock_code_eles[index].text
            stock_code_list.append(code)

        # 所有自选股的股票名字
        stock_name_eles = self.finds(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/portfolio_stockName"]')
        stock_name_list = []
        for index in range(len(stock_name_eles)):
            name = stock_name_eles[index].text
            stock_name_list.append(name)

        #根据函数的参数flag判断是否返回股票代码的列表，还是名字的列表
        if flag:
            return stock_code_list
        else:
            return stock_name_list

    def goto_manageStock(self):
        self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/edit_group"]')
        return ManageStockPage(self.driver)

    def goto_marketSearch(self):
        self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")
        return MarketSearch(self.driver)
