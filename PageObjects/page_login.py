"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 15:25
@File    : page_login.py
@Explain : 企业版登录页面
"""
from time import sleep
from PageLocators.page_login_loc import LoginPageLocs as loc
from Common.basepage import BasePage

class LoginPage(BasePage):

    def login(self,user,passwd):
        self.input_text(loc.username_loc,"登录页面_输入用户名",user)
        self.input_text(loc.passwd_loc,"登录页面_输入密码",passwd)
        self.click_element(loc.login_button_loc,"登录页面_点击登录按钮")

    # 获取用户名输入错误时的提示框
    def get_error_user_msg_from_login_area(self):
        # 等待2s，使得元素文本显示
        sleep(1)
        return self.get_text(loc.user_prompt_box_loc,"登录页面_用户名下方错误提示信息")

    # 获取密码输入错误时的提示框
    def get_error_pwd_msg_from_login_area(self):
        # 等待2s,使得元素文本显示
        sleep(1)
        return self.get_text(loc.pwd_prompt_box_loc,"登录页面_密码下方错误提示信息")

