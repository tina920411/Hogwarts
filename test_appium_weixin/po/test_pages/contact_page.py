# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2020/12/27 21:41
@File     :contact_page.py
-------------------------------
"""
from appium.webdriver.common.mobileby import MobileBy

from test_appium_weixin.po.test_pages.BaseFunctions import BasicFunction
from test_appium_weixin.po.test_pages.add_member_page import AddMember
from test_appium_weixin.po.test_pages.manage_contact import ManageContact


class ContactPage(BasicFunction):
    """
    实现两种情况来到达添加成员页面：
    1 直接往下滑屏至添加成员，并点击
    2 点击管理通讯录，到达管理通讯录页面，再点击添加成员
    """
    def goto_add_member(self):
        """
        第一种情况，直接点击添加成员操作
        :return:
        """
        # 使用下滑方法，找到添加成员按钮，并点击
        self.swipe_and_click(MobileBy.XPATH, "//*[@text='添加成员']")

        return AddMember(self.driver)


    def goto_manage_contact(self):
        """
        第二种情况，点击管理通讯录
        :return:
        """
        self.find_and_click(MobileBy.XPATH, "//*[@resource-id = 'com.tencent.wework:id/gup']")
        return ManageContact(self.driver)

    def go_back_member_list(self, dict_info):
        """
        添加成员结束后，go back到成员list中，用于获取当前所有成员的名字，用于断言
        :return:
        """
        self.wait_for(MobileBy.XPATH, "//*[@text='手动输入添加']")
        self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gu_']")
        self.wait_for(MobileBy.XPATH, "//*[contains(@text,'企业通讯录')]")
        print(self.find(MobileBy.XPATH, f"//*[@text='{dict_info['user_name']}']").text)
        return self.find(MobileBy.XPATH, f"//*[@text='{dict_info['user_name']}']").text