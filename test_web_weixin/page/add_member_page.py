# -*- coding: utf-8 -*-
#-------------------------------
# @Time: 20-12-22  下午1:06
# @Author: tina
# @File: add_member_page.py
#-------------------------------
from time import sleep

from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.contact_page import ContactPage


class AddMember(BasePage):


    def add_member(self, **dict):
        """
        添加成员操作
        :return: 返回到ContactPage()
        """

        if dict['gender'].lower() in ['man','male','boy']:
            gender = 1
        else:
            gender = 2
        if dict['status'].lower() in ['common','ordinary']:
            status = 0
        else:
            status = 1
        self.driver.find_element(By.ID, "username").send_keys(dict['name'])
        self.driver.find_element(By.ID, "memberAdd_english_name").send_keys(dict['english_name'])
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(dict['id'])
        gender_web = self.driver.find_element(By.CSS_SELECTOR, "[name='gender']")
        for index in gender_web:
            if index.get_attribute('value') == gender:
                index.click()
        sleep(1)
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(dict['tel'])
        self.driver.find_element(By.ID, "memberAdd_mail").send_keys(dict['email'])
        self.driver.find_element(By.ID, "memberAdd_title").send_keys(dict['dutity'])
        status_web = self.driver.find_element(By.CSS_SELECTOR, "[name='identity_stat']")
        for index in status_web:
            if index.get_attribute('value') == status:
                index.click()
        sleep(1)
        invit_web = self.driver.find_element(By.CSS_SELECTOR, "[name='sendInvite']")
        #如果不想发送邀请信息
        if dict['invitation_method'].lower() != 'yes' and invit_web.is_selected():
            invit_web.click()
        #如果想发送邀请信息
        elif dict['invitation_method'].lower() == 'yes' and not invit_web.is_selected():
            invit_web.click()
        #点击保存按钮
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)



    def add_member_fail(self, id, tel, email):
        """
        添加成员失败操作
        :return:返回错误提示列表
        """
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(dict['id'])
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(dict['tel'])
        self.driver.find_element(By.ID, "memberAdd_mail").send_keys(dict['email'])
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        res = self.driver.find_elements(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        error_list = [i.text for i in res]
        print(error_list)
        return error_list

    def goto_add_department(self):
        # 解决循环导入的问题
        from page.add_department_page import AddDepartment
        """
        添加部门操作
        :return: 
        """
        return AddDepartment(self.driver)






