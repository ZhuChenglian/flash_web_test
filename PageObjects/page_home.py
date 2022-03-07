"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 15:25
@File    : page_home.py
@Explain : 首页页面
"""
from PageLocators.page_home_loc import HomePageLocs as loc
from Common.basepage import BasePage
from Common.my_logger import logger

class HomePage(BasePage):

    def click_fc_download_loc(self):
        logger.info("开始进行：点击首页页面_fc下载按钮操作")
        return self.click_element(loc.fc_download_loc,"首页页面_fc下载按钮")

    def click_fp_download_loc(self):
        logger.info("开始进行：点击首页页面_flash player下载文本操作")
        return self.click_element(loc.fp_download_loc,"首页页面_flash player下载文本")

    def click_ep_download_loc(self):
        logger.info("开始进行：点击首页页面_企业版下载文本操作")
        return self.click_element(loc.ep_download_loc,"首页页面_企业版下载文本")

    def click_flash_center_loc(self):
        logger.info("开始进行：点击首页页面_导航栏flash中心操作")
        return self.click_element(loc.flash_center_loc,"首页页面_导航栏flash中心")

    def click_enterprise_loc(self):
        logger.info("开始进行：点击首页页面_导航栏企业版操作")
        return self.click_element(loc.enterprise_loc,"首页页面_导航栏企业版")

    def click_education_loc(self):
        logger.info("开始进行：点击首页页面_导航栏教育版操作")
        return self.click_element(loc.education_loc,"首页页面_导航栏教育版")

    def click_help_center_loc(self):
        logger.info("开始进行：首页页面_导航栏帮助中心操作")
        return self.click_element(loc.help_center_loc,"首页页面_导航栏帮助中心")

    def click_custom_service_loc(self):
        logger.info("开始进行：点击首页页面_导航栏客服支持操作")
        return self.click_element(loc.custom_service_loc,"首页页面_导航栏客服支持")

    def click_notice_item_loc(self):
        logger.info("开始进行：首页页面_导航栏官方公告操作")
        return self.click_element(loc.notice_item_loc,"首页页面_导航栏官方公告")




