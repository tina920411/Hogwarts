# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2020/12/27 22:02
@File     :BaseFunctions.py
-------------------------------
"""
import os
import time
from string import Template
from time import sleep

import allure
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


import inspect

from test_stronger_frame.black_handle import find_black_wrapper, click_black_wrapper


class BasicFunction:
    """
    这个类主要功能：定义各种操作页面函数，定义返回主页面函数，以及定义全部case结束后driver quit函数
    """
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        self.blackList = [
            (MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/ib_close"]'),
            (MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/tv_agree"]'),
            (MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/tv_left" and @text="下次再说"]')]



    @find_black_wrapper
    def find(self, by, location):
        return self.driver.find_element(by, location)

    def finds(self, by, location):
        return self.driver.find_elements(by, location)

    @click_black_wrapper
    def find_and_click(self, by, location):
        self.driver.find_element(by, location).click()

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

    def capture_page_screenshot(self, attach=False):
        # 每次测试的时候只要建立一个对应时间的pictures文件夹即可
        if not os.getenv('PictureLog', ''):
            self.picture_log_time = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
            self.picture_log_dir = os.path.dirname(os.getcwd()) + '/pictures/' + self.picture_log_time + '/'
            if os.path.exists(self.picture_log_dir) and os.path.isdir(self.picture_log_dir):
                pass
            else:
                os.makedirs(self.picture_log_dir)
            os.environ['PictureLog'] = self.picture_log_dir

        picture_log_dir = os.getenv("PictureLog", "")
        picture_time = time.time()
        picture_path = picture_log_dir + str(picture_time) + '.png'
        self.driver.get_screenshot_as_file(picture_path)
        if attach is True:
            with open(picture_path, "rb") as p:
                picture_data = p.read()
            allure.attach(picture_data, attachment_type=allure.attachment_type.PNG)

    def yaml_steps(self, path, send_code: str = "", send_name: str = "", flag: str = "true"):
        with open(path, encoding="UTF-8") as f:
            function_name = inspect.stack()[1].function  # 返回上一级的函数名
            read_yaml_str = f.read()
            #在yaml 文件中引用了变量， 根据形参的值对相关函数变量赋值
            tempTemplate1 = Template(read_yaml_str)
            new_f = tempTemplate1.safe_substitute(
                {f"{function_name}_StockName": send_name, f"{function_name}_StockCode": send_code})

            steps = yaml.safe_load(new_f)[function_name]
            print(steps)
            return_val_dict = {}
            for step in steps:
                if "capture_picture" in step.keys() and "yes" == step["capture_picture"]:
                    self.capture_page_screenshot(attach=True)

                # 根据股票flag，判断返回股票代码list, 还是股票名字list
                if "flag" in step.keys() and step["flag"] == flag and "keyword_steps" in step.keys():

                    if "finds" == step["keyword_steps"]["action"]:
                        return_eles = self.finds(step["keyword_steps"]["by"], step["keyword_steps"]["locator"])

                        if "capture_picture" in step["keyword_steps"].keys() and "yes" == step["keyword_steps"]["capture_picture"]:
                            self.capture_page_screenshot(attach=True)

                        for index in range(len(return_eles)):
                            code = return_eles[index].text
                            #return_val.append(code)
                            step["keyword_steps"]["return_list"].append(code)
                        return_val_dict[function_name] = step["keyword_steps"]["return_list"]
                    return return_val_dict

                #根据根据股票flag，选择代码或者名字删除的自选股
                elif "flag" in step.keys() and step["flag"] == flag and "keyword_steps" not in step.keys():

                    if "find_and_click" == step["action"]:
                        self.find_and_click(step["by"], step["locator"])
                    elif "send" == step["action"]:
                        self.find_and_send(step["by"], step["locator"], step["send"])

                #正常的find , send, click 操作
                elif "flag" not in step.keys() and "action" in step.keys() and "find_and_click" == step["action"]:

                    self.find_and_click(step["by"], step["locator"])

                #输入信息
                elif "flag" not in step.keys() and "action" in step.keys() and "send" == step["action"]:
                    self.find_and_send(step["by"], step["locator"], step["content"])
                    if "sleep" in step.keys():
                        sleep(step["sleep"])

                #是否需要等待
                elif "flag" not in step.keys() and "wait_element" in step.keys():
                    self.wait_for(step["wait_element"]["by"], step["wait_element"]["locator"])
                    if "capture_picture" in step["wait_element"].keys() and "yes" == step["wait_element"]["capture_picture"]:
                        self.capture_page_screenshot(attach=True)




