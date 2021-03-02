# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/2/20 14:18
@File     : test_department.py
-------------------------------
"""
import os

from pytest_assume.plugin import assume

from ww_request.api.DepartApi import DepartmentApi

api = DepartmentApi()
yaml_file_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestDepartment:

    def test_get_department_list(self, check_token_expire, depart_id=0):

        department_info = api.read_token_from_yaml(fr"{yaml_file_path}\data\department\get_department.yaml",
                                                   check_token_expire, id=depart_id)
        if depart_id == 0:
            del department_info["params"]["id"]
        print(department_info)
        get_r = api.check_department_api(department_info["url"], department_info["params"])
        print(get_r)
        with assume:
            assert get_r['errmsg'] == 'ok'
        with assume:
            assert get_r['errcode'] == 0

    def test_create_department(self, check_token_expire):
        depart_info = api.read_token_from_yaml(fr"{yaml_file_path}\data\department\post_department.yaml",
                                               check_token_expire)
        try:
            post_r = api.create_department_api(depart_info["url"], depart_info["req_info"])
            print(post_r)
        except Exception as e:
            print(e)
        finally:
            delete_department_info = api.read_token_from_yaml(fr"{yaml_file_path}\data\department\delete_department.yaml",
                                                              check_token_expire, id=depart_info["req_info"]["data"]["id"])
            delete_r = api.delete_department_api(delete_department_info["url"], delete_department_info["params"])
            print(delete_r)
            with assume:
                assert delete_r['errmsg'] == 'deleted'
        with assume:
            assert post_r['errcode'] == 0
            assert post_r['errmsg'] == 'created'
            assert post_r['id'] == depart_info["req_info"]["data"]["id"]