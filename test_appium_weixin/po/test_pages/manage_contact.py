# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2020/12/27 21:42
@File     :manage_contact.py
-------------------------------
"""
from appium.webdriver.common.mobileby import MobileBy

from test_appium_weixin.po.test_pages.BaseFunctions import BasicFunction
from test_appium_weixin.po.test_pages.add_member_page import AddMember


class ManageContact(BasicFunction):
    def goto_add_member_via_manageContact(self):
        """
        点击添加成员，然后return到添加成员操作页面
        :return:
        """
        self.find_and_click(MobileBy.XPATH, "//*[@text='添加成员']")
        return AddMember(self.driver)