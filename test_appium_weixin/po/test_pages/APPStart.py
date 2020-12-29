# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2020/12/27 22:02
@File     :APPStart.py
-------------------------------
"""
from appium import webdriver

from test_appium_weixin.po.test_pages.BaseFunctions import BasicFunction
from test_appium_weixin.po.test_pages.main_page import MainPage


class APP_precondition(BasicFunction):
    """
    这是一个关于启动APP, 前往Main page的类
    """

    def start_app(self):
        if self.driver is None:
            caps = {}
            caps['platformName'] = "Android"
            caps['deviceName'] = "127.0.0.1:7555"
            caps['appPackage'] = "com.tencent.wework"
            caps['appActivity'] = ".launch.LaunchSplashActivity"
            caps['noReset'] = "true"
            caps['ensureWebviewsHavePages'] = 'true'
            caps['settings[waitForIdleTimeout]'] = 0
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(30)

    def goto_mainpage(self):
        return MainPage(self.driver)
