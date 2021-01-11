# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/1/8 15:07
@File     :manageStock.py
-------------------------------
"""
from appium.webdriver.common.mobileby import MobileBy

from test_frame.BaseFunctions import BasicFunction



class ManageStockPage(BasicFunction):

    def deleteStock(self, stock, flag:bool=True):
        from test_frame.page.market import MarketPage
        #如果flag为true, 则根据股票代码删除想要删除的自选股
        if flag:
            #选中并点击股票旁边的小按钮
            self.find_and_click(MobileBy.XPATH, f'//*[@resource-id="com.xueqiu.android:id/stockCode" and @text="{stock}"]/../../..//*[@resource-id="com.xueqiu.android:id/check"]')
        else:
            #如果flag为false, 则根据股票名字删除想要删除的自选股
            self.find_and_click(MobileBy.XPATH, f'//*[@resource-id="com.xueqiu.android:id/stockName" and @text="{stock}"]/../../..//*[@resource-id="com.xueqiu.android:id/check"]')
        #点击“删除自选”
        self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/cancel_follow"]')
        self.wait_for(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/tv_title"]')
        #点击删除后会弹出是否确认删除自选股的弹框，点击确定
        self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/tv_right" and @text="确定"]')
        self.wait_for(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_close"]')
        # 点击“完成”
        self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_close"]')
        return MarketPage(self.driver)