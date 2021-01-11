# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2020/12/27 21:43
@File     :add_member_page.py
-------------------------------
"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from test_appium_weixin.po.test_pages.BaseFunctions import BasicFunction



class AddMember(BasicFunction):

    def add_member(self, dict_info, method):
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        self.find_and_send(MobileBy.XPATH, "//*[contains(@text, '姓名')]/..//*[@text='必填']", dict_info['user_name'])
        self.find_and_click(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']")
        self.wait_for(MobileBy.XPATH, "//*[@text='女']")
        self.find_and_click(MobileBy.XPATH, f"//*[@text='{dict_info['gender']}']")
        self.find_and_send(MobileBy.XPATH, "//*[contains(@text, '手机')]/..//*[@text='手机号']", dict_info['tel'])
        if dict_info['invite_method'] =='off':
            self.find_and_click(MobileBy.XPATH, "//*[@text='保存后自动发送邀请通知']")
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")
        sleep(5)

        if method == "via ContactManage":
            from test_appium_weixin.po.test_pages.manage_contact import ManageContact
            return ManageContact(self.driver)
        elif method == "via AddressList":
            from test_appium_weixin.po.test_pages.contact_page import ContactPage
            return ContactPage(self.driver)