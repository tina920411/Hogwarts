# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/2/4 14:34
@File     :DepartApi.py
-------------------------------
"""
from ww_request.api.BaseApi import AllBaseApi


class DepartmentApi(AllBaseApi):


    def check_department_api(self, url, req_dict):
        r = self.method_get(url, req_dict)
        return r

    def create_department_api(self, url, req_dict):
        r = self.method_post(url, req_dict)
        return r

    def update_department_api(self, url, req_dict):
        r = self.method_post(url, req_dict)
        return r

    def delete_department_api(self, url, req_dict):
        r = self.method_get(url, req_dict)
        return r