"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 18:05
@File    : test_nt.py
@Explain : 测试用例-官方公告
"""
import allure
import pytest
from PageObjects.page_nt import NtPage
from PageObjects.page_common import CommonPage
from Common.my_logger import logger

@allure.feature("官方公告页面-测试文本链接点击跳转功能")
@pytest.mark.run(order=14)
@pytest.mark.usefixtures("testnt_back")
class TestNt:

    @allure.story("点击官方公告页面-文章-id=178用例")
    def test_click_nt_1(self,testnt_back):

        # 官方公告文章
        try:
            NtPage(testnt_back).click_nt_art_1()
            CommonPage(testnt_back).close_switch_window()
            CommonPage(testnt_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击官方公告页面-文章-id=177用例")
    def test_click_nt_2(self,testnt_back):

        # 官方公告文章
        try:
            NtPage(testnt_back).click_nt_art_2()
            CommonPage(testnt_back).close_switch_window()
            CommonPage(testnt_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击官方公告页面-文章-id=173用例")
    def test_click_nt_3(self,testnt_back):

        # 官方公告文章
        try:
            NtPage(testnt_back).click_nt_art_3()
            CommonPage(testnt_back).close_switch_window()
            CommonPage(testnt_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击官方公告页面-文章-id=170用例")
    def test_click_nt_4(self,testnt_back):

        # 官方公告文章
        try:
            NtPage(testnt_back).click_nt_art_4()
            CommonPage(testnt_back).close_switch_window()
            CommonPage(testnt_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击官方公告页面-文章-id=157用例")
    def test_click_nt_5(self,testnt_back):

        # 官方公告文章
        try:
            NtPage(testnt_back).click_nt_art_5()
            CommonPage(testnt_back).close_switch_window()
            CommonPage(testnt_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击官方公告页面-文章-id=154用例")
    def test_click_nt_6(self,testnt_back):

        # 官方公告文章
        try:
            NtPage(testnt_back).click_nt_art_6()
            CommonPage(testnt_back).close_switch_window()
            CommonPage(testnt_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击官方公告页面-文章-id=153用例")
    def test_click_nt_7(self,testnt_back):

        # 官方公告文章
        try:
            NtPage(testnt_back).click_nt_art_7()
            CommonPage(testnt_back).close_switch_window()
            CommonPage(testnt_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击官方公告页面-文章-id=144用例")
    def test_click_nt_8(self,testnt_back):

        # 官方公告文章
        try:
            NtPage(testnt_back).click_nt_art_8()
            CommonPage(testnt_back).close_switch_window()
            CommonPage(testnt_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击官方公告页面-文章-id=143用例")
    def test_click_nt_9(self,testnt_back):

        # 官方公告文章
        try:
            NtPage(testnt_back).click_nt_art_9()
            CommonPage(testnt_back).close_switch_window()
            CommonPage(testnt_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击官方公告页面-文章-id=140用例")
    def test_click_nt_10(self,testnt_back):

        # 官方公告文章
        try:
            NtPage(testnt_back).click_nt_art_10()
            CommonPage(testnt_back).close_switch_window()
            CommonPage(testnt_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击官方公告页面-文章-id=138用例")
    def test_click_nt_11(self,testnt_back):

        # 官方公告文章
        try:
            NtPage(testnt_back).click_nt_art_11()
            CommonPage(testnt_back).close_switch_window()
            CommonPage(testnt_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")


