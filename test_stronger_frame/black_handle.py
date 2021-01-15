# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/1/8 13:12
@File     :black_handle.py
-------------------------------
"""
from test_stronger_frame.StrongerFrameLogger import CustomLogger

logger = CustomLogger.onelogger()

def find_black_wrapper(fun):
    def magic(*args, **kwargs):
        print("++++++++")
        print(args[0])
        from test_frame.BaseFunctions import BasicFunction
        self: BasicFunction = args[0]
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            logger.info("查找元素出现异常，待检查是否出现黑名单元素")
            self.capture_page_screenshot(attach=True)
            for black_ele in self.blackList:
                #查找黑名单中的成员是否在页面中
                print(black_ele)
                ele = self.finds(*black_ele)
                print("===========")
                print(ele)
                if len(ele) > 0:
                    #如果在页面中，则click 掉该元素
                    ele[0].click()
                    print("正在进行black elements的click")
                    #然后继续查找想要的元素
                    return magic(*args, **kwargs)
            #如果黑名单中的元素没有找到，则抛出异常
            logger.error(f"没有找到黑名单元素，抛出异常-->{e}")
            raise e
    return magic

def click_black_wrapper(fun):
    def magic(*args, **kwargs):

        from test_frame.BaseFunctions import BasicFunction
        self: BasicFunction = args[0]
        try:
            fun(*args, **kwargs)
        except Exception as e:
            logger.info("查找元素出现异常，待检查是否出现黑名单元素")
            self.capture_page_screenshot(attach=True)
            for black_ele in self.blackList:
                #查找黑名单中的成员是否在页面中

                ele = self.finds(*black_ele)
                print("===========")
                if len(ele) > 0:
                    #如果在页面中，则click 掉该元素
                    ele[0].click()
                    print("正在进行black element的click")
                    #然后继续查找想要的元素
                    return magic(*args, **kwargs)
            #如果黑名单中的元素没有找到，则抛出异常
            logger.error(f"没有找到黑名单元素，抛出异常-->{e}")
            raise e
    return magic
