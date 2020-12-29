# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2020/12/27 22:02
@File     :BaseFunctions.py
-------------------------------
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasicFunction():
    """
    这个类主要功能：定义各种操作页面函数，定义返回主页面函数，以及定义全部case结束后driver quit函数
    """
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, location):
        return self.driver.find_element(by, location)


    def find_and_click(self, by, location):
        self.find(by, location).click()

    def find_and_send(self, by, location, text):
        self.find(by, location).send_keys(text)

    def swipe_and_find(self, by, location):
        self.driver.implicitly_wait(1)
        elements = self.driver.find_elements(by, location)
        #print(elements)
        while len(elements) == 0:
            self.driver.swipe(0, 600, 0, 400)
            elements = self.driver.find_elements(by, location)
        self.driver.implicitly_wait(20)
        #print(elements[0])
        return elements[0]

    def swipe_and_click(self, by, location):
        self.swipe_and_find(by, location).click()

    def scroll_and_find(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                             'scrollable(true).instance(0)).'
                                                             'scrollIntoView(new UiSelector().'
                                                             f'text("{text}").instance(0));')

    def scroll_and_click(self, text):
        self.scroll_and_find(text).click()

    def wait_for(self, by, location):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((by, location)))

    def go_back_main_page(self):
        self.find_and_click(MobileBy.XPATH, "//*[ @resource-id = 'com.tencent.wework:id/dqn' and @text = '消息']")

    def quit(self):
        self.driver.quit()
