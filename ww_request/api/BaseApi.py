# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/2/4 14:32
@File     :BaseApi.py
-------------------------------
"""
import copy
import json
from string import Template

import requests
import yaml


class AllBaseApi:
    """
    这个基础类实现了公共类所有Api的功能, 是其他Api的符类
    包含以下功能：
                       1.
    """

    def __init__(self):
        self.session = requests.Session()

    def get_token(self, path, fixture_name):
        member_info = self.read_token_from_yaml(path, fixture_name)
        return member_info["token"]


    def method_get(self, url, kwargs):
        """
        req传入的数据类型如下
       :param :
       req_dict={
              "params": {
              "access_token": $token
              "userid": '002'
              }
        }
        :return: r, json格式的get返回值
        """
        params = copy.deepcopy(kwargs)
        if 'headers' in kwargs:
            headers = params['headers']
            del params['headers']
            r = self.session.get(url, params=params, headers=headers)
        else:
            r = self.session.get(url, params=params).json()
        return r

    def method_post(self, url, kwargs):
        payload = copy.deepcopy(kwargs)
        if 'access_token' in kwargs:
            self.token = kwargs['access_token']
            params = {"access_token": self.token}
            del payload['access_token']
            print(type(payload))
            print(payload)

            r = self.session.post(url, params=params, data=json.dumps(payload['data'])).json()
            return r
        else:
            print("need set token key in yaml file")
            raise KeyError

    def method_delete(self, url, kwargs):

        r = self.session.delete(url, params=kwargs).json()
        return r


    def method_put(self):
        pass

    def read_token_from_yaml(self, path, fixture_name, id = ""):
        with open(f"{path}", "r", encoding="UTF-8") as f:
            # 利用Template技术替换yaml文件中的token变量
            tempTemplate = Template(f.read())
            # c类型为str类型， <class 'str'>
            if id == "" or id == 0:
                c = tempTemplate.safe_substitute({"token": fixture_name})
            else:
                c = tempTemplate.safe_substitute({"token": fixture_name, "id": id})
            # 将yaml文件数据，转换成python类型，比如 <class 'dict'>
            member_info = yaml.safe_load(c)
            print(member_info)
            # 返回yaml中
        return member_info
