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
    def get_contact_info_add_member():
        with open("contact_info_add_member.yaml", encoding="UTF-8") as f:
            contact_info_add_member = yaml.safe_load(f)
            print(contact_info_add_member)
            info_datas = contact_info_add_member["datas"]
            info_ids = contact_info_add_member["ids"]
            return [info_datas, info_ids]
    def get_contact_info_by_contact():
        with open("contact_info_by_contact.yaml", encoding="UTF-8") as f:
            contact_info_by_contact = yaml.safe_load(f)
            print(contact_info_by_contact)
            info_datas = contact_info_by_contact["datas"]
            info_ids = contact_info_by_contact["ids"]
            return [info_datas, info_ids]
    def get_contact_info_fail():
        with open("contact_info_fail.yaml", encoding="UTF-8") as f:
            contact_info_fail = yaml.safe_load(f)
            info_datas = contact_info_fail["datas"]
            info_ids = contact_info_fail["ids"]
            return [info_datas, info_ids]

    def setup(self):
        #第一次实例化
        self.main = MainPage()
    def teardown(self):
        self.main.driver.quit()

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('dict',
                             get_contact_info_add_member()[0],ids=get_contact_info_add_member()[1])
    def test_add_member(self, dict):
        """
        成功添加测试用例
        :return:
        """
        #1. 跳转到添加成员页面  2. 添加成员操作   3. 自动跳转到通讯录页面并返回成员列表
        res = self.main.goto_add_member().add_member(dict).get_member()
        assert str(dict['tel']) in res

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('dict', get_contact_info_by_contact()[0], ids=get_contact_info_by_contact()[1])
    def test_add_member_by_contact(self, dict):
        """
        通过通讯录页面添加成员
        :return:
        """
        res = self.main.goto_contact().goto_add_member().add_member(dict).get_member()
        assert str(dict['tel']) in res

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('dict', get_contact_info_fail()[0], ids=get_contact_info_fail()[1])
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

    @pytest.mark.run(order=1)
    def test_add_department(self):
        depart_list = self.main.goto_contact().goto_add_department().add_department().get_depart_list()
        assert "技术部" in depart_list

if __name__ == '__main__':
    pytest.main("test_web_weixin.py", "-sv")












