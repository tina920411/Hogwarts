# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2020/12/29 16:51
@File     :conftest.py
-------------------------------
"""
import pytest

from test_appium_weixin.po.test_pages.APPStart import APP_precondition


@pytest.fixture()
def myfixture():
    print("*************开始操作**************")
    app_precondition = APP_precondition()
    app_precondition.start_app()
    yield app_precondition
    app_precondition.go_back_main_page()
    print("*************操作结束**************")
    app_precondition.quit()
    print()


