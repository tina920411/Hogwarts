# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2020/12/27 13:17
@File     :test_weixin_daka.py
-------------------------------
"""
import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWeiXinDaKa:

    def setup(self):
        caps = {}
        caps['platformName'] = "Android"
        caps['deviceName'] = "127.0.0.1:7555"
        #caps['platformVersion'] = "6.0.1"
        caps['appPackage'] = "com.tencent.wework"
        caps['appActivity'] = ".launch.LaunchSplashActivity"
        caps['noReset'] = "true"
        # caps['skipServerInstallation'] = 'true'
        # caps['skipDeviceInitialization'] = 'true'
        caps['ensureWebviewsHavePages'] = 'true'
        #caps['dontStopAppOnReset'] = 'true'
        caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        #查找滚动元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '次外出')]").click()
        time.sleep(2)
        print(self.driver.page_source)
        WebDriverWait(self.driver, 10).until(lambda x:"外出打卡成功" in x.page_source)
        assert "外出打卡成功" in self.driver.page_source

if __name__ == '__main__':
    pytest.main(["test_weixin_daka.py", "-sv"])