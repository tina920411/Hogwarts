# -*- coding: utf-8 -*-
#-------------------------------
# @Time: 20-12-22  下午1:06
# @Author: tina
# @File: main_page.py
#-------------------------------
from selenium.webdriver.common.by import By

from page.add_member_page import AddMember
from page.base_page import BasePage
from page.contact_page import ContactPage


class MainPage(BasePage):

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:AddMember
        """
        self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        return AddMember(self.driver)



    def goto_contact(self):
        """
        跳转到通讯录页面
        :return: ContactPage(self.driver)
        """
        self.driver.find_element(By.ID, "menu_contacts").click()
        return ContactPage(self.driver)



