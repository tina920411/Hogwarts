# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/1/10 11:23
@File     :test_add_delete_stock.py
-------------------------------
"""
from test_frame.APPStart import APP_precondition


class TestAddDeleteStock:
    def setup(self):
        self.app_precondition = APP_precondition()
        self.app_precondition.start_app()

    def test_add_stock(self):


       stocks = self.app_precondition.goto_mainpage().goto_search().select_SelfStock("jingdong", "JD").goto_market().stocktList()
       assert "JD" in stocks

    def test_delete_stock(self):
        result = self.app_precondition.goto_mainpage().goto_market().goto_manageStock().deleteStock("JD").stocktList()
        assert "JD" not in result
