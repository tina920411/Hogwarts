# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/2/5 17:32
@File     :test_member.py
-------------------------------
"""
import os
from string import Template

import pytest
import requests
import yaml

from pytest_assume.plugin import assume

from ww_request.api.MemberApi import MemberApi

###定义一个全局变量api, 使得下面所有的测试用例或者其他函数或方法都可以调用
api = MemberApi()
yaml_file_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def setup_module():
    print("测试开始...")

def teardown_module():
    print("测试结束...")


class TestMember:

    def test_get_member(self, check_token_expire, user_id=""):
        """
        :param check_token_expire: it is a fixture function in conftest.py
        :param user_id: 传递想要获取成员信息的userid
        :return:
        """
        user_id = "HuangTingTing"

        member_info = api.read_token_from_yaml(fr"{yaml_file_path}/data/member/get_member.yaml",
                                               check_token_expire, id=user_id)

        r = api.check_member_api(member_info["url"], member_info["params"])
        print(r)
        with assume:
            assert r['errmsg'] == 'ok'
        with assume:
            assert r['userid'] == user_id

    def test_create_member(self, check_token_expire):
        """
        create 一位成员后，
        需要再对该成员进行delete,
        避免用例之间的依赖关系
        :param check_token_expire: it is a fixture function in conftest.py
        """
        member_info = api.read_token_from_yaml(fr"{yaml_file_path}/data/member/post_member.yaml",
                                               check_token_expire)
        try:
            r = api.create_member_api(member_info["url"], member_info["req_info"])
            print(r)
            with assume:
                assert r['errmsg'] == 'created'
        except Exception as e:
            print(e)
        finally:
            ###对上面create的动作进行清理，以免影响后面的测试用例
            delete_member_info = api.read_token_from_yaml(
                fr"{yaml_file_path}/data/member/delete_member.yaml",
                check_token_expire, id=member_info["req_info"]["data"]["userid"])

            r = api.delete_member_api(delete_member_info["url"], delete_member_info["params"])

            print(r)
            with assume:
                assert r['errmsg'] == 'deleted'

    def test_delete_member(self, check_token_expire):
        """
        在测试删除成员用例的时候，
        最好先create 一位成员，
        然后再对该成员进行delete,
        避免用例之间的依赖关系
        :param check_token_expire: it is a fixture function in conftest.py
        """
        member_info = api.read_token_from_yaml(fr"{yaml_file_path}/data/member/post_member.yaml",
                                               check_token_expire)
        try:

            r = api.create_member_api(member_info["url"], member_info["req_info"])
            with assume:
                assert r['errmsg'] == 'created'

        except Exception as e:
            print(e)

        finally:

            delete_member_info = api.read_token_from_yaml(
                fr"{yaml_file_path}/data/member/delete_member.yaml",
                check_token_expire, id=member_info["req_info"]["data"]["userid"])

            r = api.delete_member_api(delete_member_info["url"], delete_member_info["params"])

            print(r)
            with assume:
                assert r['errmsg'] == 'deleted'

    def test_update_member(self, check_token_expire):
        """
        1、先create one member
        2、update member
        3、delete member
        :param check_token_expire: it is a fixture function in conftest.py
        """
        create_member_info = api.read_token_from_yaml(fr"{yaml_file_path}/data/member/post_member.yaml",
                                                      check_token_expire)
        update_member_info = api.read_token_from_yaml(fr"{yaml_file_path}/data/member/update_member.yaml",
                                                      check_token_expire)
        try:
            create_r = api.create_member_api(create_member_info["url"], create_member_info["req_info"])
            print(create_r)
            with assume:
                assert create_r['errmsg'] == 'created'
            update_r = api.update_member_api(update_member_info["url"], update_member_info["req_info"])
            print(update_r)
        except Exception as e:
            print(e)

        finally:

            delete_member_info = api.read_token_from_yaml(
                fr"{yaml_file_path}/data/member/delete_member.yaml",
                check_token_expire, id=update_member_info["req_info"]["data"]["userid"])

            r = api.delete_member_api(delete_member_info["url"], delete_member_info["params"])
            print(r)
            with assume:
                assert r['errmsg'] == 'deleted'

def get_negative_info(path):
    """
    这个函数主要作用是读取negative member info，为后面集中run negative类型的测试用例提供info
    :param path:
    :return:
    """
    #1. 取出token_param.yaml中的token值
    with open(fr"{yaml_file_path}/testcase/token_param.yaml", "r", encoding="UTF-8") as f:
        f_info = yaml.safe_load(f)
        token = f_info["token"]
        print(token)
    #2. 替换negative_member_info.yaml中的token变量，并读取yaml文件中的所有数据
    negative_create_member_info = api.read_token_from_yaml(path, token)
    negetive_info = negative_create_member_info["negetive_info"]
    ids = negative_create_member_info["ids"]
    #print([negetive_info, ids])
    return [negetive_info, ids]

class TestNegativeMember:

    @pytest.mark.parametrize(
        "allinfo",
        get_negative_info(fr"{yaml_file_path}/data/member/negative_member_info.yaml")[0],
        ids=get_negative_info(fr"{yaml_file_path}/data/member/negative_member_info.yaml")[1])
    def test_negative_create_member(self, allinfo, check_token_expire):

        #1. 先使用negative info create member， 然后记录errcode 和 errmsg

        local_token = api.get_token(fr"{yaml_file_path}/testcase/token_param.yaml", check_token_expire)

        print(allinfo)
        url = allinfo["url"]
        allinfo["req_info"]["access_token"] = local_token
        data = allinfo["req_info"]
        print(data)
        errcode = allinfo["errcode"]
        errmsg = allinfo["errmsg"]
        # 执行api create member
        r = api.create_member_api(url, data)
        print(r['errcode'])
        print(r['errmsg'])

        #2. 先尝试读取刚刚create negative member的userid, 如果能够读取成功，则先删除，防止影响后面的测试用例
        try:
            member_info = api.read_token_from_yaml(fr"{yaml_file_path}/data/member/get_member.yaml",
                                                   check_token_expire, id=allinfo["req_info"]["data"]["userid"])

            get_r = api.check_member_api(member_info["url"], member_info["params"])
            #print(get_r)
            if get_r['errmsg'] == 'ok':

                delete_member_info = api.read_token_from_yaml(
                    fr"{yaml_file_path}/data/member/delete_member.yaml",
                    check_token_expire, id=allinfo["req_info"]["data"]["userid"])

                delete_r = api.delete_member_api(delete_member_info["url"], delete_member_info["params"])

        except Exception as e:
            print(e)
        #3. 最后对测试用例进行assert判断
        with assume:
            assert r['errcode'] == errcode
        with assume:
            assert errmsg in r['errmsg']

