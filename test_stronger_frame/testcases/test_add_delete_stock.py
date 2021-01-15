# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/1/10 11:23
@File     :test_add_delete_stock.py
-------------------------------
"""
import os
import time

import allure
import pytest
import yaml

from test_stronger_frame.APPStart import APP_precondition

@allure.feature("添加或删除自选股模块")
class TestAddDeleteStock:

    def get_stock_info():
        with open("G:\project\Hogwarts\\test_stronger_frame\\testcases\stock_info.yaml", encoding="UTF-8") as f:
            stock_info = yaml.safe_load(f)
            datas = stock_info["datas"]
            ids = stock_info["ids"]
            return stock_info

    def setup_class(self):
        self.app_precondition = APP_precondition()
        self.app_precondition.start_app()

    @allure.story("添加自选股")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "stock_code, stock_name",
        get_stock_info()["datas"],
        ids=get_stock_info()["ids"]
    )
    def test_add_stock(self, stock_code, stock_name):

       stocks = self.app_precondition.goto_mainpage().goto_search().select_SelfStock(stock_code, stock_name).goto_market().stocktList()
       assert stock_code in stocks

    @allure.story("删除自选股")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "stock_code, stock_name",
        get_stock_info()["datas"],
        ids=get_stock_info()["ids"]
    )
    def test_delete_stock(self, stock_code, stock_name):

        result = self.app_precondition.goto_mainpage().goto_market().goto_manageStock().deleteStock(stock_code).stocktList()
        assert stock_code not in result
