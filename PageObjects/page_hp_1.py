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

class HpPage_1(BasePage):

    def click_help_data_1(self):
        logger.info("开始进行：点击帮助中心页面-安装与更新问题文本操作")
        return self.click_element(loc.help_data_loc_1,"帮助中心页面-安装与更新问题文本")

    def click_art_1(self):
        logger.info("开始进行：点击帮助中心页面-安装与更新问题-文章-id=16操作")
        return self.click_element(loc.help_art_loc_1_1,"帮助中心页面-安装与更新问题-文章-id=16")

    def click_art_2(self):
        logger.info("开始进行：点击帮助中心页面-安装与更新问题-文章-id=62操作")
        return self.click_element(loc.help_art_loc_1_2,"帮助中心页面-安装与更新问题-文章-id=62")

    def click_art_3(self):
        logger.info("开始进行：点击帮助中心页面-安装与更新问题-文章-id=63操作")
        return self.click_element(loc.help_art_loc_1_3,"帮助中心页面-安装与更新问题-文章-id=63")

    def click_art_4(self):
        logger.info("开始进行：点击帮助中心页面-安装与更新问题-文章-id=64操作")
        return self.click_element(loc.help_art_loc_1_4,"帮助中心页面-安装与更新问题-文章-id=64")

    def click_art_5(self):
        logger.info("开始进行：点击帮助中心页面-安装与更新问题-文章-id=68操作")
        return self.click_element(loc.help_art_loc_1_5,"帮助中心页面-安装与更新问题-文章-id=68")

    def click_art_6(self):
        logger.info("开始进行：点击帮助中心页面-安装与更新问题-文章-id=111操作")
        return self.click_element(loc.help_art_loc_1_6,"帮助中心页面-安装与更新问题-文章-id=111")

    def click_art_7(self):
        logger.info("开始进行：点击帮助中心页面-安装与更新问题-文章-id=112操作")
        return self.click_element(loc.help_art_loc_1_7,"帮助中心页面-安装与更新问题-文章-id=112")

    def click_art_8(self):
        logger.info("开始进行：点击帮助中心页面-安装与更新问题-文章-id=113操作")
        return self.click_element(loc.help_art_loc_1_8,"帮助中心页面-安装与更新问题-文章-id=113")
