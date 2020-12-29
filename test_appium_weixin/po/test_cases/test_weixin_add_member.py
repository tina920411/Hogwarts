# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2020/12/29 16:03
@File     :test_weixin_add_member.py
-------------------------------
"""
import pytest
import yaml



class TestWeiXinAddMember:
    """
    目前先写添加正确的cases，后续再添加negative cases
    """
    def get_member_info():
        with open("member_info_success.yaml", encoding="utf-8") as f:
            member_info = yaml.safe_load(f)
            print(member_info)
            info_datas = member_info["datas"]
            info_ids = member_info["ids"]
            return [info_datas, info_ids]

    @pytest.mark.parametrize('dict_info', get_member_info()[0], ids=get_member_info()[1])
    def test_add_member_viaContact_success(self, dict_info, myfixture):

        result = myfixture.goto_mainpage().goto_ContactPage().goto_add_member().add_member(dict_info).go_back_member_list(dict_info)
        assert result == str(dict_info['user_name'])
        
    def test_add_member_viaManageContact_syccess(self):
        """
        :return:
        """
        pass

    def test_delete_member(self):
        pass
