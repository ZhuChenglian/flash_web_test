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

class HpPage_6(BasePage):

    def click_help_data_10(self):
        logger.info("开始进行：点击帮助中心页面-Flash不可用问题文本操作")
        return self.click_element(loc.help_data_loc_10,"帮助中心页面-Flash不可用问题文本")

    def click_art_1(self):
        logger.info("开始进行：点击帮助中心页面-Flash不可用问题-文章-id=61操作")
        return self.click_element(loc.help_art_loc_10_1,"帮助中心页面-Flash不可用问题-文章-id=61")

    def click_art_2(self):
        logger.info("开始进行：点击帮助中心页面-Flash不可用问题-文章-id=62操作")
        return self.click_element(loc.help_art_loc_10_2,"帮助中心页面-Flash不可用问题-文章-id=62")

    def click_art_3(self):
        logger.info("开始进行：点击帮助中心页面-Flash不可用问题-文章-id=64操作")
        return self.click_element(loc.help_art_loc_10_3,"帮助中心页面-Flash不可用问题-文章-id=64")

    def click_art_4(self):
        logger.info("开始进行：点击帮助中心页面-Flash不可用问题-文章-id=66操作")
        return self.click_element(loc.help_art_loc_10_4,"帮助中心页面-Flash不可用问题-文章-id=66")

    def click_art_5(self):
        logger.info("开始进行：点击帮助中心页面-Flash不可用问题-文章-id=68操作")
        return self.click_element(loc.help_art_loc_10_5,"帮助中心页面-Flash不可用问题-文章-id=68")

    def click_art_6(self):
        logger.info("开始进行：点击帮助中心页面-Flash不可用问题-文章-id=115操作")
        return self.click_element(loc.help_art_loc_10_6,"帮助中心页面-Flash不可用问题-文章-id=115")

    def click_art_7(self):
        logger.info("开始进行：点击帮助中心页面-Flash不可用问题-文章-id=148操作")
        return self.click_element(loc.help_art_loc_10_7,"帮助中心页面-Flash不可用问题-文章-id=148")
