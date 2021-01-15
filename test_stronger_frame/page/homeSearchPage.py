# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/1/11 20:00
@File     :homeSearchPage.py
-------------------------------
"""
from test_stronger_frame.BaseFunctions import BasicFunction
from test_stronger_frame.StrongerFrameLogger import CustomLogger

logger = CustomLogger.onelogger()

class HomeSearchPage(BasicFunction):
    def search_handle(self, send_code):
        self.yaml_steps('../page/homeSearchPage.yaml', send_code=send_code)

    def select_SelfStock(self, send_code, send_name: str = ""):
        # 防止循环导入
        from test_stronger_frame.page.mainPage import MainPage

        # 加入自选股股票

        logger.info("点击自选股按钮，加入自选股股票")
        self.yaml_steps('../page/homeSearchPage.yaml', send_code=send_code, send_name=send_name)

        return MainPage(self.driver)