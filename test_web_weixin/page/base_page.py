# -*- coding: utf-8 -*-
#-------------------------------
# @Time: 20-12-22  下午1:05
# @Author: tina
# @File: base_page.py
#-------------------------------

import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, base_driver=None):
        base_driver:WebDriver
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            self.__cookin_login()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(5)

    def __cookie_login(self):
        #cookie 列表式登录
        with open("cookie_data.yaml", encoding="utf-8") as f:
            yaml_cookie_data = yaml.safe_load(f)
            for cookie in yaml_cookie_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

