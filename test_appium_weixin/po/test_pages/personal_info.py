# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2020/12/30 14:56
@File     :personal_info.py
-------------------------------
"""
from appium.webdriver.common.mobileby import MobileBy

from test_appium_weixin.po.test_pages.BaseFunctions import BasicFunction
from test_appium_weixin.po.test_pages.edit_personal_info import Edit_Personal_Page


class Personal_Info_Page(BasicFunction):

    def goto_edit_personal_info(self, dict_info):

        self.wait_for(MobileBy.XPATH, f"//*[@text='{dict_info['user_name']}']")
        self.find_and_click(MobileBy.XPATH, "//*[@text='个人信息']/../../../../..//*[@resource-id='com.tencent.wework:id/guk']")
        self.wait_for(MobileBy.XPATH, "//*[@text='编辑成员']")
        self.find_and_click(MobileBy.XPATH, "//*[@text='编辑成员']")
        return Edit_Personal_Page(self.driver)



