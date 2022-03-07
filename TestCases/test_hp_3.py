"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 18:02
@File    : test_hp_3.py
@Explain : 测试用例-帮助中心-Flash运行异常
"""
import allure
import pytest
from PageObjects.page_hp_3 import HpPage_3
from PageObjects.page_common import CommonPage
from Common.my_logger import logger

@allure.feature("帮助中心页面-测试文本链接点击跳转功能")
@pytest.mark.run(order=9)
@pytest.mark.usefixtures("testhp_back")
class TestHp_3:

    @allure.story("点击帮助中心页面-安装与更新问题-文章用例")
    def test_click_hp_1(self,testhp_back):

        # Flash中心使用指南
        try:
            HpPage_3(testhp_back).click_help_data_3()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        # Flash中心使用指南-文章-id=142
        try:
            HpPage_3(testhp_back).click_art_1()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        try:
            HpPage_3(testhp_back).click_art_2()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        try:
            HpPage_3(testhp_back).click_art_3()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        try:
            HpPage_3(testhp_back).click_art_4()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        try:
            HpPage_3(testhp_back).click_art_5()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        try:
            HpPage_3(testhp_back).click_art_6()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        try:
            HpPage_3(testhp_back).click_art_7()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        try:
            HpPage_3(testhp_back).click_art_8()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        try:
            HpPage_3(testhp_back).click_art_9()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        try:
            HpPage_3(testhp_back).click_art_10()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        try:
            HpPage_3(testhp_back).click_art_11()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        try:
            HpPage_3(testhp_back).click_art_12()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        try:
            HpPage_3(testhp_back).click_art_13()
            CommonPage(testhp_back).close_switch_window()
            CommonPage(testhp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")
