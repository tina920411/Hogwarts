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
from test_appium_weixin.po.test_pages.edit_personal_info import Edit_Personal_Page


class ManageContact(BasicFunction):

    def member_infoList_viaManageContact(self, dict_info):
        """
        用于delete成员后， check 成员是否在列表中
        :param dict_info:
        :return:
        """
        self.driver.implicitly_wait(1)
        page_source = self.driver.page_source
        # 从管理通讯录页面到返回通讯录页面
        self.find_and_click(MobileBy.XPATH,
                            "//*[@text='管理通讯录']/../../../../..//*[@resource-id='com.tencent.wework:id/guk']")
        self.wait_for(MobileBy.XPATH, "//*[ @resource-id = 'com.tencent.wework:id/dqn' and @text = '通讯录']")
        return page_source

    def goto_add_member_via_manageContact(self):
        """
        点击添加成员，然后return到添加成员操作页面
        :return:
        """
        self.find_and_click(MobileBy.XPATH, "//*[@text='添加成员']")
        return AddMember(self.driver)

    def goto_edit_personal_info_via_manageContact(self, dict_info):
        """
        从管理通讯录处，单击相关人员的编辑按钮，并返回到编辑成员的页面
        :return:
        """
        self.find_and_click(MobileBy.XPATH, f"//*[@text='{dict_info['user_name']}']/../../../..//*[@resource-id='com.tencent.wework:id/fcq']")
        return Edit_Personal_Page(self.driver)

    def go_back_memberManage_list(self, dict_info):
        """
        添加成员结束后，go back到管理通讯录list中，用于获取当前所有成员的名字，用于断言
        :return:
        """
        self.wait_for(MobileBy.XPATH, "//*[@text='手动输入添加']")
        self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gu_']")
        self.wait_for(MobileBy.XPATH, "//*[@text='管理通讯录']")
        print(self.find(MobileBy.XPATH, f"//*[@text='{dict_info['user_name']}']").text)

        #返回通讯录页面
        self.find_and_click(MobileBy.XPATH, "//*[@text='管理通讯录']/../../../../..//*[@resource-id='com.tencent.wework:id/guk']")
        self.wait_for(MobileBy.XPATH, "//*[ @resource-id = 'com.tencent.wework:id/dqn' and @text = '通讯录']")

        return self.find(MobileBy.XPATH, f"//*[@text='{dict_info['user_name']}']").text
