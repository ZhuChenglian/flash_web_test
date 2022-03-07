"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 15:25
@File    : page_hp_1.py
@Explain : 帮助中心页面
"""
from PageLocators.page_hp_loc import HpPageLocs as loc
from Common.basepage import BasePage
from Common.my_logger import logger

class HpPage_5(BasePage):

    def click_help_data_5(self):
        logger.info("开始进行：点击帮助中心页面-常见问题文本操作")
        return self.click_element(loc.help_data_loc_5,"帮助中心页面-常见问题文本")

    def click_art_1(self):
        logger.info("开始进行：点击帮助中心页面-常见问题-文章-id=16操作")
        return self.click_element(loc.help_art_loc_5_1,"帮助中心页面-常见问题-文章-id=16")

    def click_art_2(self):
        logger.info("开始进行：点击帮助中心页面-常见问题-文章-id=55操作")
        return self.click_element(loc.help_art_loc_5_2,"帮助中心页面-常见问题-文章-id=55")

    def click_art_3(self):
        logger.info("开始进行：点击帮助中心页面-常见问题-文章-id=62操作")
        return self.click_element(loc.help_art_loc_5_3,"帮助中心页面-常见问题-文章-id=62")

    def click_art_4(self):
        logger.info("开始进行：点击帮助中心页面-常见问题-文章-id=63操作")
        return self.click_element(loc.help_art_loc_5_4,"帮助中心页面-常见问题-文章-id=63")

    def click_art_5(self):
        logger.info("开始进行：点击帮助中心页面-常见问题-文章-id=64操作")
        return self.click_element(loc.help_art_loc_5_5,"帮助中心页面-常见问题-文章-id=64")

    def click_art_6(self):
        logger.info("开始进行：点击帮助中心页面-常见问题-文章-id=67操作")
        return self.click_element(loc.help_art_loc_5_6,"帮助中心页面-常见问题-文章-id=67")

    def click_art_7(self):
        logger.info("开始进行：点击帮助中心页面-常见问题-文章-id=68操作")
        return self.click_element(loc.help_art_loc_5_7,"帮助中心页面-常见问题-文章-id=68")

    def click_art_8(self):
        logger.info("开始进行：点击帮助中心页面-常见问题-文章-id=115操作")
        return self.click_element(loc.help_art_loc_5_8,"帮助中心页面-常见问题-文章-id=115")

    def click_art_9(self):
        logger.info("开始进行：点击帮助中心页面-常见问题-文章-id=175操作")
        return self.click_element(loc.help_art_loc_5_9,"帮助中心页面-常见问题-文章-id=175")
