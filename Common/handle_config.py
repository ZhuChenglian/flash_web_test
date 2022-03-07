"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/2/25 11:29
@File    : handle_config.py
"""
import os
from configparser import ConfigParser
from Common.handle_path import conf_dir

class HandleConfig(ConfigParser):

    def __init__(self,file_path):
        super(HandleConfig,self).__init__()
        self.read(file_path,encoding="utf-8")

file_path = os.path.join(conf_dir,"config.ini")
conf = HandleConfig(file_path)

