"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/2/25 11:29
@File    : my_logger.py
"""
import os
import logging
from Common.handle_config import conf
from Common.handle_path import logs_dir

class MyLogger(logging.Logger):

    def __init__(self,name,level=logging.INFO,file=None):
        super().__init__(name,level)

        fmt = "%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d行：%(message)s "
        formatter = logging.Formatter(fmt)

        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        if file:
            handle2 = logging.FileHandler(file,encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)

if conf.getboolean("log","file_ok"):
    file_name = os.path.join(logs_dir,conf.get("log","file_name"))
else:
    file_name = None

logger = MyLogger(conf.get("log","name"),conf.get("log","level"),file_name)
