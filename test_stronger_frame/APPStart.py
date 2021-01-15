# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/1/11 20:04
@File     :APPStart.py
-------------------------------
"""
from appium import webdriver

from test_stronger_frame.BaseFunctions import BasicFunction
from test_stronger_frame.page.mainPage import MainPage


class APP_precondition(BasicFunction):
    """
    这是一个关于启动APP的类
    """

    def start_app(self):
        if self.driver is None:
            caps = {
                "platformName": "Android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "noReset": "True"
            }

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)


    def goto_mainpage(self):
        #进入到首页

        return MainPage(self.driver)
