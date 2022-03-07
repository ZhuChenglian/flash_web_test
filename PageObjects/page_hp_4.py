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

class HpPage_4(BasePage):

    def click_help_data_4(self):
        logger.info("开始进行：点击帮助中心页面-版本问题文本操作")
        return self.click_element(loc.help_data_loc_4,"帮助中心页面-版本问题文本")

    def click_art_1(self):
        logger.info("开始进行：点击帮助中心页面-版本问题-文章-id=16操作")
        return self.click_element(loc.help_art_loc_4_1,"帮助中心页面-版本问题-文章-id=167")

    def click_art_2(self):
        logger.info("开始进行：点击帮助中心页面-版本问题-文章-id=62操作")
        return self.click_element(loc.help_art_loc_4_2,"帮助中心页面-版本问题-文章-id=166")

    def click_art_3(self):
        logger.info("开始进行：点击帮助中心页面-版本问题-文章-id=63操作")
        return self.click_element(loc.help_art_loc_4_3,"帮助中心页面-版本问题-文章-id=168")

    def click_art_4(self):
        logger.info("开始进行：点击帮助中心页面-版本问题-文章-id=64操作")
        return self.click_element(loc.help_art_loc_4_4,"帮助中心页面-版本问题-文章-id=31")

    def click_art_5(self):
        logger.info("开始进行：点击帮助中心页面-版本问题-文章-id=68操作")
        return self.click_element(loc.help_art_loc_4_5,"帮助中心页面-版本问题-文章-id=61")

    def click_art_6(self):
        logger.info("开始进行：点击帮助中心页面-版本问题-文章-id=111操作")
        return self.click_element(loc.help_art_loc_4_6,"帮助中心页面-版本问题-文章-id=66")

    def click_art_7(self):
        logger.info("开始进行：点击帮助中心页面-版本问题-文章-id=112操作")
        return self.click_element(loc.help_art_loc_4_7,"帮助中心页面-版本问题-文章-id=169")


