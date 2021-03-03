# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/2/5 16:27
@File     :conftest.py
-------------------------------
"""
import os
import time

import pytest
import requests
import yaml

yaml_file_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture(scope="module", autouse=True)
def check_token_expire():
    secretId = "S0SuApuyPSfu5SpMDHo9WUULk2wWTha2gPxJkXAasIs"
    corpid = "ww5513aee450ec644e"
    params = {
        "corpid": corpid,
        "corpsecret": secretId
    }
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    api_check_token = requests.Session()

    now_time = int(time.time())
    with open(fr"{yaml_file_path}/ww_request/testcase/token_param.yaml", "r", encoding="UTF-8") as f:
        token_info = yaml.safe_load(f)
    #判断yaml文件中是否有token值，如果没有，则request.get，拿一下token，并写入到yaml中
    if token_info["token"] is None:

        result = api_check_token.get(url=url, params=params).json()
        print(result['access_token'])
        timestrap = int(time.time())
        token_info["token"] = result['access_token']
        token_info["expire_time"] = 7200
        token_info["start_time"] = int(time.time())
        token_info["start_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestrap))
        with open(fr"{yaml_file_path}/ww_request/testcase/token_param.yaml", "w+", encoding="UTF-8") as f:
            yaml.safe_dump(token_info, f)

    #如果yaml文件中有token值， 判断获取的时长是否大于7200， 如果超时了，则重新获取token并写入， 否则跳过。
    else:
        timeArray = time.strptime(token_info["start_time"], "%Y-%m-%d %H:%M:%S")
        token_get_timestrap = int(time.mktime(timeArray))
        if (now_time - token_get_timestrap) > int(token_info["expire_time"]):
            result_new = api_check_token.get(url=url, params=params).json()
            token_info["token"] = result_new['access_token']
            token_info["start_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time())))
            with open(fr"{yaml_file_path}/ww_request/testcase/token_param.yaml", "w+", encoding="UTF-8") as f:
                yaml.safe_dump(token_info, f)
        else:
            pass
    yield token_info["token"]

