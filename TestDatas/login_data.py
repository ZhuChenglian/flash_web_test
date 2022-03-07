"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/2/25 11:42
@File    : login_data.py [企业版登录数据]
"""
valid_user = ("15618275180","123456")

invalid_data_user = [
    {"user": "15618275181", "passwd": "123456", "check": "用户名不存在或密码不正确"},
    {"user": "15618275180", "passwd": "12345678", "check": "用户名不存在或密码不正确"},
    {"user": "15618278956", "passwd": "123456", "check": "用户名不存在或密码不正确"},
    {"user": "", "passwd": "123456", "check": "手机号不能为空"}
]

invalid_data_pwd = [{"user": "15618275180", "passwd": "", "check": "密码不能为空"}]
