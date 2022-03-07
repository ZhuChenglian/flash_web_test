"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 18:02
@File    : test_en.py
@Explain : 测试用例-企业版
"""
import allure
import pytest
from time import sleep
from PageObjects.page_en import EnPage
from PageObjects.page_common import CommonPage
from Common.my_logger import logger

@allure.feature("企业版页面-测试按钮和文本点击跳转功能")
@pytest.mark.run(order=5)
@pytest.mark.usefixtures("testen_back")
class TestEd:

    @allure.story("点击企业版页面-立即咨询按钮用例")
    def test_click_ed_1(self,testen_back):
        # 点击立即申请按钮
        try:
            EnPage(testen_back).click_en_1()
            sleep(10)
            CommonPage(testen_back).close_switch_window()
            # 获取当前窗口的句柄
            CommonPage(testen_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击企业版页面-立即购买按钮用例")
    def test_click_ed_2(self,testen_back):
        # 点击立即申请按钮
        try:
            EnPage(testen_back).click_en_2()
            # 获取当前窗口的句柄
            CommonPage(testen_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        try:
            EnPage(testen_back).click_en_3()
            CommonPage(testen_back).close_switch_window()
            CommonPage(testen_back).close_switch_window()
            CommonPage(testen_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")
