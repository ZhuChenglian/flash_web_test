"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/2/25 11:44
@File    : global_data.py
"""
import os

base_url = "https://www.flash.cn/"

# 企业版登录页面地址
login_url = os.path.join(base_url,"enterprise/login.html")
# fp页面地址
fp_url = os.path.join(base_url,"download-wins")
# fc页面地址
fc_url = "https://soft.flash.cn/flashcenter/index.html"
# 企业版页面地址
en_url = os.path.join(base_url,"enterprise/index")
# 教育版页面地址
ed_url = os.path.join(base_url,"education/index")
# 帮助中心页面地址
hp_url = os.path.join(base_url,"support/help.html")
# 客服支持页面地址
cs_url = os.path.join(base_url,"custom-service/index")
# 官方公告页面地址
nt_url = os.path.join(base_url,"notice/notice-item")

# 通用的普通用户
user = ("15618275180","123456")

