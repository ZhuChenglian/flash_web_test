"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 18:02
@File    : test_home.py
@Explain : 测试用例-首页
"""
import allure
import pytest
from PageObjects.page_home import HomePage
from PageObjects.page_common import CommonPage
from Common.my_logger import logger

@allure.feature("flash官网首页-测试文本链接点击跳转功能")
@pytest.mark.run(order=2)
@pytest.mark.usefixtures("testhome_back")
class TestHome:

    @allure.story("点击首页-立即下载按钮-用例")
    def test_click_home_1(self,testhome_back):
        try:
            # 点击首页-立即下载按钮
            HomePage(testhome_back).click_fc_download_loc()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.feature("flash官网首页-测试文本链接点击跳转功能")
    def test_click_home_2(self, testhome_back):
        try:
            # 点击flash player下载文本链接
            HomePage(testhome_back).click_fp_download_loc()
            # 获取新窗口句柄并切换到新窗口，然后关闭当前窗口
            CommonPage(testhome_back).close_switch_window()
            # 获取当前窗口的句柄
            CommonPage(testhome_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击企业版授权下载文本链接-用例")
    def test_click_home_3(self, testhome_back):
        try:
            # 点击企业版授权下载文本链接
            HomePage(testhome_back).click_ep_download_loc()
            # 获取新窗口句柄并切换到新窗口，然后关闭当前窗口
            CommonPage(testhome_back).close_switch_window()
            # 获取当前窗口的句柄
            CommonPage(testhome_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击首页导航栏-flash中心文本-用例")
    def test_click_home_4(self, testhome_back):
        try:
            # 点击首页导航栏-flash中心文本链接
            HomePage(testhome_back).click_flash_center_loc()
            # 获取新窗口句柄并切换到新窗口，然后关闭当前窗口
            CommonPage(testhome_back).close_switch_window()
            # 获取当前窗口的句柄
            CommonPage(testhome_back).switch_window_no_close()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击首页导航栏-企业版文本-用例")
    def test_click_home_5(self, testhome_back):
        try:
            # 点击首页导航栏-企业版文本
            HomePage(testhome_back).click_enterprise_loc()
            # 返回上一页
            CommonPage(testhome_back).back_last_page()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击首页导航栏-教育版文本-用例")
    def test_click_home_6(self, testhome_back):
        try:
            # 点击首页导航栏-教育版文本
            HomePage(testhome_back).click_education_loc()
            # 返回上一页
            CommonPage(testhome_back).back_last_page()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    # @allure.story("点击首页导航栏-帮助中心-用例")
    def test_click_home_7(self, testhome_back):
        try:
            # 点击首页导航栏-帮助中心
            HomePage(testhome_back).click_help_center_loc()
            # 返回上一页
            CommonPage(testhome_back).back_last_page()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击首页导航栏-客服支持-用例")
    def test_click_home_8(self, testhome_back):
        try:
            # 点击首页导航栏-客服支持
            HomePage(testhome_back).click_custom_service_loc()
            # 返回上一页
            CommonPage(testhome_back).back_last_page()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

    @allure.story("点击首页导航栏-官方公告-用例")
    def test_click_home_9(self, testhome_back):
        # 点击首页导航栏-官方公告
        try:
            HomePage(testhome_back).click_notice_item_loc()
        except:
            logger.exception("当前用例执行失败，点击页面有报错\n")
            raise
        else:
            logger.info("当前用例执行成功，页面点击跳转成功\n")

