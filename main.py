"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/2/25 11:44
@File    : main.py
"""
import pytest

pytest.main(["-s", "-v","--html=Outputs/html/pytest.html", "--alluredir=Outputs/allure"])

