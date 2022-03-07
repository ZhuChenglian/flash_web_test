"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 18:02
@File    : test_fp.py
@Explain : 测试用例-fp页面
"""
import allure
import pytest
from PageObjects.page_fp import FpPage
from PageObjects.page_common import CommonPage
from Common.my_logger import logger

@allure.feature("FP页面-测试按钮和文本点击跳转功能")
@pytest.mark.run(order=3)
@pytest.mark.usefixtures("testfp_back")
class TestFp:

    @allure.story("点击fp页面-fc下载按钮用例")
    def test_click_fp_1(self,testfp_back):
        # 点击立即申请按钮
        try:
            FpPage(testfp_back).click_fp_1()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，文件下载成功\n")

    @allure.story("点击fp页面_ax版本下载最新版用例")
    def test_click_fp_2(self,testfp_back):
        # 点击立即申请按钮
        try:
            FpPage(testfp_back).click_fp_2()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，文件下载成功\n")

    @allure.story("点击fp页面_pp版本下载最新版用例")
    def test_click_fp_3(self,testfp_back):
        # 点击立即申请按钮
        try:
            FpPage(testfp_back).click_fp_3()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，文件下载成功\n")

    @allure.story("点击fp页面_np版本下载最新版用例")
    def test_click_fp_4(self,testfp_back):
        # 点击立即申请按钮
        try:
            FpPage(testfp_back).click_fp_4()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，文件下载成功\n")

    @allure.story("点击fp页面_MAC pp下载用例")
    def test_click_fp_5(self,testfp_back):
        # 点击立即申请按钮
        try:
            FpPage(testfp_back).click_fp_5()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，文件下载成功\n")

    @allure.story("点击fp页面_MAC np下载用例")
    def test_click_fp_6(self,testfp_back):
        # 点击立即申请按钮
        try:
            FpPage(testfp_back).click_fp_6()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，文件下载成功\n")

    @allure.story("点击fp页面_咨询客服按钮用例")
    def test_click_fp_7(self,testfp_back):
        # 点击立即申请按钮
        try:
            FpPage(testfp_back).click_fp_7()
            CommonPage(testfp_back).close_switch_window()
            CommonPage(testfp_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面跳转成功\n")
