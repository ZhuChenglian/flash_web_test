"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 15:26
@File    : page_nt.py
@Explain : 官方公告页面
"""
from PageLocators.page_nt_loc import NtPageLocs as loc
from Common.basepage import BasePage
from Common.my_logger import logger

class NtPage(BasePage):

    def click_nt_art_1(self):
        logger.info("开始进行：点击官方公告页面-文章-id=178操作")
        return self.click_element(loc.notice_art_loc_1, "官方公告页面-文章-id=178")

    def click_nt_art_2(self):
        logger.info("开始进行：点击官方公告页面-文章-id=177操作")
        return self.click_element(loc.notice_art_loc_2, "官方公告页面-文章-id=177")

    def click_nt_art_3(self):
        logger.info("开始进行：点击官方公告页面-文章-id=173操作")
        return self.click_element(loc.notice_art_loc_3, "官方公告页面-文章-id=173")

    def click_nt_art_4(self):
        logger.info("开始进行：点击官方公告页面-文章-id=170操作")
        return self.click_element(loc.notice_art_loc_4, "官方公告页面-文章-id=170")

    def click_nt_art_5(self):
        logger.info("开始进行：点击官方公告页面-文章-id=157操作")
        return self.click_element(loc.notice_art_loc_5, "官方公告页面-文章-id=157")

    def click_nt_art_6(self):
        logger.info("开始进行：点击官方公告页面-文章-id=154操作")
        return self.click_element(loc.notice_art_loc_6, "官方公告页面-文章-id=154")

    def click_nt_art_7(self):
        logger.info("开始进行：点击官方公告页面-文章-id=153操作")
        return self.click_element(loc.notice_art_loc_7, "官方公告页面-文章-id=153")

    def click_nt_art_8(self):
        logger.info("开始进行：点击官方公告页面-文章-id=144操作")
        return self.click_element(loc.notice_art_loc_8, "官方公告页面-文章-id=144")

    def click_nt_art_9(self):
        logger.info("开始进行：点击官方公告页面-文章-id=143操作")
        return self.click_element(loc.notice_art_loc_9, "官方公告页面-文章-id=143")

    def click_nt_art_10(self):
        logger.info("开始进行：点击官方公告页面-文章-id=140操作")
        return self.click_element(loc.notice_art_loc_10, "官方公告页面-文章-id=140")

    def click_nt_art_11(self):
        logger.info("开始进行：点击官方公告页面-文章-id=138操作")
        return self.click_element(loc.notice_art_loc_11, "官方公告页面-文章-id=138")