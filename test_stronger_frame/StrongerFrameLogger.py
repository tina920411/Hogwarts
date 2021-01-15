# -*- coding: utf-8 -*-
"""
-------------------------------
@Author   : Tina Huang
@Time     : 2021/1/14 13:54
@File     :MyLogger.py
-------------------------------
"""
import logging
import os
import time


class CustomLogger:
    def onelogger():
        logger = logging.getLogger("mylog")
        log_dir = os.path.dirname(os.getcwd()) + '/logs/'
        if os.path.exists(log_dir) and os.path.isdir(log_dir):
            pass
        else:
            os.makedirs(log_dir)
        if not logger.handlers:
            logger.setLevel(logging.INFO)  #log等级总开关

            log_time = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
            log_name = log_dir + log_time + '.log'
            logfile = log_name
            #设置日志格式
            log_format = '[%(asctime)s - %(filename)s(line:%(lineno)d)] - %(levelname)s: %(message)s'
            formatter = logging.Formatter(fmt=log_format)
            logging.basicConfig(format=log_format, datefmt='%Y-%m-%d %H:%M:%S', filename=logfile, filemode='w')

            #创建FileHandler
            fh = logging.FileHandler(logfile)
            fh.setLevel(logging.INFO)
            fh.setFormatter(formatter)
            logger.addHandler(fh)

            #创建StreamHandler
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            ch.setFormatter(formatter)
            logger.addHandler(ch)

        return logger



