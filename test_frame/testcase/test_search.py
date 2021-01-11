# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/1/10 15:43
@File     :test_search.py
-------------------------------
"""
from test_frame.APPStart import APP_precondition


class TestSearch:

    def testSearch(self):
        app_precondition = APP_precondition()
        app_precondition.start_app()
        app_precondition.goto_mainpage().goto_market().goto_marketSearch().search()