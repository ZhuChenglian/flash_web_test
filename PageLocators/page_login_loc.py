"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 11:38
@File    : page_login_loc.py
@Explain : 企业版登录页面元素定位
"""
from selenium.webdriver.common.by import By

class LoginPageLocs:

    # 用户名输入框
    username_loc = (By.XPATH, '//input[@class="en-log-name"]')
    # 密码输入框
    passwd_loc = (By.XPATH, '//input[@class="en-log-password"]')
    # 登录按钮
    login_button_loc = (By.XPATH, '//span[@class="en-log-btn"]')
    # 用户名下方提示语
    user_prompt_box_loc = (By.XPATH,'//input[@class="en-log-name"]/parent::div[@class="en-log-item"]/following-sibling::p')
    # 密码下方提示语
    pwd_prompt_box_loc = (By.XPATH,'//input[@class="en-log-password"]/parent::div[@class="en-log-item"]/following-sibling::p')

