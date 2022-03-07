"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 18:02
@File    : test_login.py
@Explain : 测试用例-企业版登录
"""
import allure
import pytest
from PageObjects.page_login import LoginPage
from PageObjects.page_en import EnPage
from TestDatas import login_data as ld
from Common.my_logger import logger

@allure.feature("企业版登录页面-测试用户登录功能")
@pytest.mark.run(order=1)
@pytest.mark.usefixtures("testlogin_back")
class TestLogin:
    # 异向场景 - 登录失败 - 数据格式无效

    @allure.story("登录功能-用户名下方错误提示用例")
    @pytest.mark.parametrize("case",ld.invalid_data_user)
    def test_login_fail_invalid_data_user(self,case,testlogin_back):
        LoginPage(testlogin_back).login(case["user"],case["passwd"])
        try:
            assert LoginPage(testlogin_back).get_error_user_msg_from_login_area() == case["check"]
        except:
            logger.exception("当前用例执行失败，断言不通过\n")
        else:
            logger.info("当前用例执行成功，断言通过\n")

    @allure.story("登录功能-密码下方错误提示用例")
    @pytest.mark.parametrize("case",ld.invalid_data_pwd)
    def test_login_fail_invalid_data_pwd(self,case,testlogin_back):
        LoginPage(testlogin_back).login(case["user"],case["passwd"])
        try:
            assert LoginPage(testlogin_back).get_error_pwd_msg_from_login_area() == case["check"]
        except:
            logger.exception("当前用例执行失败，断言不通过\n")
        else:
            logger.info("当前用例执行成功，断言通过\n")

    # 正向场景 - 登录成功
    @allure.story("登录功能-登录成功用例")
    def test_login_success(self,testlogin_back):
        LoginPage(testlogin_back).login(*ld.valid_user)
        try:
            assert EnPage(testlogin_back).is_exit_exist()
        except:
            logger.exception("当前用例执行失败，断言不通过\n")
        else:
            logger.info("当前用例执行成功，断言通过\n")
