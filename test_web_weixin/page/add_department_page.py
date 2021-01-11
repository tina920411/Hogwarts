# -*- coding: utf-8 -*-
#-------------------------------
# @Time: 20-12-22  下午1:09
# @Author: tina
# @File: add_department_page.py
#-------------------------------
from test_web_weixin.page.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select


class AddDepartment(BasePage):


    def add_department(self):
        from test_web_weixin.page.contact_page import ContactPage
        """
        从添加成员入口处添加部门
        :return: 返回部门列表
        """
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js_create_party").click()
        self.driver.find_element(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body .qui_inputText.ww_inputText").send_keys("技术部")
        self.driver.find_element(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body .js_parent_party_name").click()
        #select_depart.deselect_by_index(1)
        self.driver.find_element(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688853359102494_anchor']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".qui_dialog_foot.ww_dialog_foot [d_ck='submit']").click()
        sleep(2)
        return ContactPage(self.driver)

    def goto_add_member(self):
        #解决循环导入的问题
        from test_web_weixin.page.add_member_page import AddMember
        """
        添加成员操作
        :return: 返回添加成员方法
        """
        self.driver.find_element(By.CSS_SELECTOR, ".qui_btn.ww_btn.js_add_member").click()
        return AddMember(self.driver)
