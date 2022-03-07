"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/2/25 11:29
@File    : handle_path.py
"""
import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)

# 测试用例路径
case_dir = os.path.join(base_dir,"TestCases")

# 测试数据的路径
datas_dir = os.path.join(base_dir,"TestDatas")

# 日志路径
logs_dir = os.path.join(base_dir,"Outputs","log")

# 配置文件路径
conf_dir = os.path.join(base_dir,"Conf")

# 页面截图路径
screenshot_dir = os.path.join(base_dir,"Outputs","screenshot")

