# -*- coding: utf-8 -*-
#-------------------------------
# @Time: 20-12-22  下午1:06
# @Author: tina
# @File: contact_page.py
#-------------------------------
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage



class ContactPage(BasePage):

    def goto_add_member(self):
        #解决循环导入的问题
        from page.add_member_page import AddMember
        """
        点击添加成员按钮
        :return: 返回添加成员方法
        """
        WebDriverWait(self.driver, 9).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".ww_operationBar .js_add_member")))
        self.driver.find_element(By.CSS_SELECTOR,".ww_operationBar .js_add_member").click()
        return AddMember(self.driver)

    def get_member(self):
        """
        获取成员列表中的手机号，用来做断言信息
        :return: 返回成员列表
        """
        sleep(2)
        self.driver.find_element(By.ID, "menu_contacts").click()
        member_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(5)")
        member_list_res = [i.text for i in member_list]
        print(member_list_res)
        return member_list_res

    def goto_add_department(self):
        from page.add_department_page import AddDepartment
        """
        添加部门操作
        :return: 
        """
        return AddDepartment(self.driver)

    def get_depart_list(self):
        """
        获取部门列表，并返回列表用于做断言信息
        :return:
        """
        departs = self.driver.find_elements(By.CSS_SELECTOR, ".jstree-anchor")
        depart_list = [i.text for i in departs]
        print(depart_list)
        return depart_list
