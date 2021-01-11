# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2020/12/30 14:57
@File     :edit_personal_info.py
-------------------------------
"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from test_appium_weixin.po.test_pages.BaseFunctions import BasicFunction



class Edit_Personal_Page(BasicFunction):
    """
    编辑个人信息页面，可以更新信息，还可以删除该成员
    """

    def delete_persion(self, method):
        """
        根据删除成员的路径，来判断返回的页面
        :param method:
        :return:
        """
        self.find_and_click(MobileBy.XPATH, "//*[@text='删除成员']")
        self.find_and_click(MobileBy.XPATH, "//*[@text='确定']")
        sleep(12)
        if method == "via ContactManage":
            from test_appium_weixin.po.test_pages.manage_contact import ManageContact
            return ManageContact(self.driver)
        elif method == "via AddressList":
            from test_appium_weixin.po.test_pages.contact_page import ContactPage
            return ContactPage(self.driver)



