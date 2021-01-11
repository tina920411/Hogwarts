# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/1/8 14:13
@File     :home_search.py
-------------------------------
"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from test_frame.BaseFunctions import BasicFunction


class HomeSearchPage(BasicFunction):
    def search_handle(self, send_text):
        self.find_and_send(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]', send_text)

    def select_SelfStock(self, send_text, stock_code):
        #防止循环导入
        from test_frame.page.main import Main

        #step1: 查找想要的自选股股票
        self.find(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/home_search"]')
        self.find_and_click(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/home_search"]')
        #sleep(3)
        self.driver.find_element(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]').send_keys(send_text)
        #self.find_and_send(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]', send_text)
        sleep(1)

        self.find_and_click(MobileBy.XPATH, f'//*[@resource-id="com.xueqiu.android:id/code" and @text="{stock_code}"]')

        self.wait_for(MobileBy.XPATH, '//*[@text="加自选"]')

        #step2: 将其加入到自选股中
        self.find_and_click(MobileBy.XPATH, f'//*[@resource-id="com.xueqiu.android:id/stockCode" and @text="{stock_code}"]/../../..//*[@resource-id="com.xueqiu.android:id/follow_btn" and @text="加自选"]')

        #step3: 会弹出是否评价雪球，，将这一行为加入到黑名单中， 并点击“下次再说”, 然后点击右上角取消，回到Main Page
        #self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_close" and @text="下次再说"]')
        self.find(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_close" and @text="取消"]')
        #print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        #print(self.driver.page_source)
        self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_close" and @text="取消"]')

        return Main(self.driver)

