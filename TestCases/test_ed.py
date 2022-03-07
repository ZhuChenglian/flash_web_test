"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 18:03
@File    : test_ed.py
@Explain : 测试用例-教育版
"""
import allure
import pytest
from PageObjects.page_ed import EdPage
from PageObjects.page_common import CommonPage
from Common.my_logger import logger

@allure.feature("教育版页面-测试按钮和文本点击跳转功能")
@pytest.mark.run(order=6)
@pytest.mark.usefixtures("tested_back")
class TestEd:

    @allure.story("点击教育版页面-立即申请按钮用例")
    def test_click_ed_1(self,tested_back):
        # 点击立即申请按钮
        try:
            EdPage(tested_back).click_ed_1()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        # 点击模板下载文本
        try:
            EdPage(tested_back).click_ed_2()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        # 点击进入企业版文本
        try:
            EdPage(tested_back).click_ed_3()
            # 获取新窗口句柄并切换到新窗口，然后关闭当前窗口
            CommonPage(tested_back).close_switch_window()
            # 获取新窗口句柄并切换到新窗口，然后关闭当前窗口
            CommonPage(tested_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

        # 点击关闭按钮
        try:
            EdPage(tested_back).click_ed_4()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

