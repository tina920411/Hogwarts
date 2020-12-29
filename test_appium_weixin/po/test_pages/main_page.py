# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2020/12/27 21:39
@File     :main_page.py
-------------------------------
"""
from appium.webdriver.common.mobileby import MobileBy

from test_appium_weixin.po.test_pages.BaseFunctions import BasicFunction
from test_appium_weixin.po.test_pages.contact_page import ContactPage


class MainPage(BasicFunction):

    def goto_ContactPage(self):
        """
        起始页的动作，点击通讯录
        """
        self.find_and_click(MobileBy.XPATH, "//*[ @resource-id = 'com.tencent.wework:id/dqn' and @text = '通讯录']")

        return ContactPage(self.driver)

