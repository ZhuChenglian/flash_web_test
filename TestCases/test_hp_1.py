"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 18:02
@File    : test_hp_1.py
@Explain : 测试用例-帮助中心-安装与更新问题
"""
import allure
import pytest
from PageObjects.page_hp_1 import HpPage_1
from PageObjects.page_common import CommonPage
from Common.my_logger import logger

@allure.feature("帮助中心页面-测试文本链接点击跳转功能")
@pytest.mark.run(order=7)
@pytest.mark.usefixtures("testhp_back")
class TestHp_1:

    @allure.story("点击帮助中心页面-安装与更新问题-文章-id=16用例")
    def test_click_hp_1(self,testhp_back):
        # 安装与更新问题-文章-id=16
        try:
            HpPage_1(testhp_back).click_art_1()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击帮助中心页面-安装与更新问题-文章-id=62用例")
    def test_click_hp_2(self,testhp_back):
        # 安装与更新问题-文章-id=16
        try:
            HpPage_1(testhp_back).click_art_2()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击帮助中心页面-安装与更新问题-文章-id=63用例")
    def test_click_hp_3(self,testhp_back):
        # 安装与更新问题-文章-id=16
        try:
            HpPage_1(testhp_back).click_art_3()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击帮助中心页面-安装与更新问题-文章-id=64用例")
    def test_click_hp_4(self,testhp_back):
        # 安装与更新问题-文章-id=16
        try:
            HpPage_1(testhp_back).click_art_4()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击帮助中心页面-安装与更新问题-文章-id=68用例")
    def test_click_hp_5(self,testhp_back):
        # 安装与更新问题-文章-id=16
        try:
            HpPage_1(testhp_back).click_art_5()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击帮助中心页面-安装与更新问题-文章-id=111用例")
    def test_click_hp_6(self,testhp_back):
        # 安装与更新问题-文章-id=16
        try:
            HpPage_1(testhp_back).click_art_6()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击帮助中心页面-安装与更新问题-文章-id=112用例")
    def test_click_hp_7(self,testhp_back):
        # 安装与更新问题-文章-id=16
        try:
            HpPage_1(testhp_back).click_art_7()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击帮助中心页面-安装与更新问题-文章-id=113用例")
    def test_click_hp_8(self,testhp_back):
        # 安装与更新问题-文章-id=16
        try:
            HpPage_1(testhp_back).click_art_8()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

