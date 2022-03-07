"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 18:02
@File    : test_cs.py
@Explain : 测试用例-客服支持
"""
import allure
import pytest
from time import sleep
from PageObjects.page_cs import CsPage
from PageObjects.page_common import CommonPage
from Common.my_logger import logger

@allure.feature("客服支持页面-测试文本链接点击跳转功能")
@pytest.mark.run(order=13)
@pytest.mark.usefixtures("testcs_back")
class TestCs:

    @allure.story("点击客服支持页面-客服支持按钮用例")
    def test_click_cs_1(self,testcs_back):
        # 点击客服支持按钮
        try:
            CsPage(testcs_back).click_cs_1()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        # 弹窗-文章-id=125
        try:
            CsPage(testcs_back).click_cs_2()
            CommonPage(testcs_back).close_switch_window()
            CommonPage(testcs_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        # 弹窗-文章-id=16
        try:
            CsPage(testcs_back).click_cs_3()
            CommonPage(testcs_back).close_switch_window()
            CommonPage(testcs_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        # 弹窗-文章-id=63
        try:
            CsPage(testcs_back).click_cs_4()
            CommonPage(testcs_back).close_switch_window()
            CommonPage(testcs_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        # 弹窗-文章-id=31
        try:
            CsPage(testcs_back).click_cs_5()
            CommonPage(testcs_back).close_switch_window()
            CommonPage(testcs_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        # 联系客服按钮
        try:
            CsPage(testcs_back).click_cs_6()
            sleep(15)
            CommonPage(testcs_back).close_switch_window()
            CommonPage(testcs_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        # 关闭按钮
        try:
            CsPage(testcs_back).click_cs_7()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击客服支持页面-文章-id=16用例")
    def test_click_cs_2(self,testcs_back):
        try:
            CsPage(testcs_back).click_cs_8()
            CommonPage(testcs_back).close_switch_window()
            CommonPage(testcs_back).switch_window()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击客服支持页面-文章-id=55用例")
    def test_click_cs_3(self,testcs_back):
        try:
            CsPage(testcs_back).click_cs_9()
            CommonPage(testcs_back).close_switch_window()
            CommonPage(testcs_back).switch_window()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击客服支持页面-文章-id=62用例")
    def test_click_cs_4(self,testcs_back):
        try:
            CsPage(testcs_back).click_cs_10()
            CommonPage(testcs_back).close_switch_window()
            CommonPage(testcs_back).switch_window()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击客服支持页面-文章-id=63用例")
    def test_click_cs_5(self,testcs_back):
        try:
            CsPage(testcs_back).click_cs_11()
            CommonPage(testcs_back).close_switch_window()
            CommonPage(testcs_back).switch_window()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击客服支持页面-文章-id=64用例")
    def test_click_cs_6(self,testcs_back):
        try:
            CsPage(testcs_back).click_cs_12()
            CommonPage(testcs_back).close_switch_window()
            CommonPage(testcs_back).switch_window()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击客服支持页面-文章-id=67用例")
    def test_click_cs_7(self,testcs_back):
        try:
            CsPage(testcs_back).click_cs_13()
            CommonPage(testcs_back).close_switch_window()
            CommonPage(testcs_back).switch_window()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")



