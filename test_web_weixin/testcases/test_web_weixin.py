# -*- coding:utf-8 -*-
#---------------------------------
#@Time     :2020/12/22 22:48
#@Author   :Administrator
#@File     :test_web_weixin.py
#---------------------------------
from page.main_page import MainPage
import pytest
import yaml


class TestWebWeixin:
    def get_contact_info_add_member(self):
        with open("contact_info_add_member.yaml", encoding="UTF-8") as f:
            contact_info_add_member = yaml.safe_load(f)
            print(contact_info_add_member)
            return contact_info_add_member
    def get_contact_info_by_contact(self):
        with open("contact_info_by_contact.yaml", encoding="UTF-8") as f:
            contact_info_by_contact = yaml.safe_load(f)
            print(contact_info_by_contact)
            return contact_info_by_contact
    def get_contact_info_fail(self):
        with open("contact_info_fail.yaml", encoding="UTF-8") as f:
            contact_info_fail = yaml.safe_load(f)
            print(contact_info_fail)
            return contact_info_fail



    def setup(self):
        #第一次实例化
        self.main = MainPage()
    @pytest.mark.parametrize('dict',
                             get_contact_info_add_member()[0],ids=get_contact_info_add_member()[1])
    def test_add_member(self, dict):
        """
        成功添加测试用例
        :return:
        """
        #1. 跳转到添加成员页面  2. 添加成员操作   3. 自动跳转到通讯录页面并返回成员列表
        res = self.main.goto_add_member().add_member(dict).get_member()
        assert tel in res

    @pytest.mark.parametrize('dict', get_contact_info_by_contact()[0], ids=get_contact_info_by_contact()[1])
    def test_add_member_by_contact(self, dict):
        """
        通过通讯录页面添加成员
        :return:
        """
        res = self.main.goto_contact().goto_add_member().add_member(dict).get_member()
        assert tel in res

    def test_add_member_fail(self, dict):
        """
        验证各种警告信息
        :param id: id 信息
        :param tel: 手机号信息
        :param email: 邮箱
        :return:
        """
        res = self.main.goto_add_member().add_member_fail(dict)
        assert dict['expect_res'] in res












