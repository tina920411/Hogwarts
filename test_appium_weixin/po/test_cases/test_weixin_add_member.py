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
import allure



class TestWeiXinAddMember:
    """
    目前先写添加正确的cases，后续再添加negative cases
    """
    def get_member_info(path):
        with open(f"{path}", encoding="utf-8") as f:
            member_info = yaml.safe_load(f)
            print(member_info)
            info_datas = member_info["datas"]
            info_ids = member_info["ids"]
            return [info_datas, info_ids]


    #@allure.feature("从通讯录添加成员")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('dict_info', get_member_info(path="member_info_success.yaml")[0],
                             ids=get_member_info(path="member_info_success.yaml")[1])
    def test_add_member_viaContact_success(self, dict_info, myfixture):

        result = myfixture.goto_mainpage().goto_ContactPage().goto_add_member().add_member(dict_info, "via AddressList").go_back_member_list(dict_info)
        assert result == str(dict_info['user_name'])




    #@allure.feature("从管理通讯录添加成员")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('dict_info', get_member_info(path="member_info_viaContactManage.yaml")[0],
                             ids=get_member_info(path="member_info_viaContactManage.yaml")[1])
    def test_add_member_viaManageContact_syccess(self, dict_info, myfixture):
        """
        :return:
        """
        result = myfixture.goto_mainpage().goto_ContactPage().goto_manage_contact().goto_add_member_via_manageContact().add_member(dict_info, "via ContactManage").go_back_memberManage_list(dict_info)
        assert result == str(dict_info['user_name'])


    #@allure.feature("从通讯录路径删除成员")
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('dict_info', get_member_info(path="member_info_success.yaml")[0],
                             ids=get_member_info(path="member_info_success.yaml")[1])
    def test_delete_member_viaAddressList(self, dict_info, myfixture):
        result = myfixture.goto_mainpage().goto_ContactPage().goto_personal_info_via_ContactPage(dict_info).goto_edit_personal_info(dict_info).delete_persion("via AddressList").member_infoList_viaAdressList(dict_info)
        assert dict_info['user_name'] not in result




    #@allure.feature("从管理通讯录路径删除成员")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('dict_info', get_member_info(path="member_info_viaContactManage.yaml")[0],
                             ids=get_member_info(path="member_info_viaContactManage.yaml")[1])
    def test_delete_member_viaManageContact(self, dict_info, myfixture):
        result = myfixture.goto_mainpage().goto_ContactPage().goto_manage_contact().goto_edit_personal_info_via_manageContact(dict_info).delete_persion("via ContactManage").member_infoList_viaManageContact(dict_info)
        assert dict_info['user_name'] not in result
