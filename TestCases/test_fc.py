"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 18:02
@File    : test_fc.py
@Explain : 测试用例-fc页面
"""
import allure
import pytest
from PageObjects.page_fc import FcPage
from Common.my_logger import logger

@allure.feature("FC页面-测试按钮和文本点击跳转功能")
@pytest.mark.run(order=4)
@pytest.mark.usefixtures("testfc_back")
class TestFc:

    @allure.story("点击fc页面-上方立即体验按钮用例")
    def test_click_fc_1(self,testfc_back):
        # 点击立即申请按钮
        try:
            FcPage(testfc_back).click_fc_1()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，文件下载成功\n")

    @allure.story("点击fc页面-下方立即体验按钮用例")
    def test_click_fc_2(self,testfc_back):
        # 点击立即申请按钮
        try:
            FcPage(testfc_back).click_fc_2()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，文件下载成功\n")

