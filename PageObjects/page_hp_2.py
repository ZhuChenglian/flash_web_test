"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 15:25
@File    : page_hp_2.py
@Explain : 帮助中心页面
"""
from PageLocators.page_hp_loc import HpPageLocs as loc
from Common.basepage import BasePage
from Common.my_logger import logger

class HpPage_2(BasePage):

    def click_help_data_2(self):
        logger.info("开始进行：点击帮助中心页面-Flash中心使用指南文本操作")
        return self.click_element(loc.help_data_loc_2,"帮助中心页面-Flash中心使用指南文本")

    def click_art_1(self):
        logger.info("开始进行：点击帮助中心页面-Flash中心使用指南-文章-id=142操作")
        return self.click_element(loc.help_art_loc_2_1,"帮助中心页面-Flash中心使用指南-文章-id=142")

    def click_art_2(self):
        logger.info("开始进行：点击帮助中心页面-Flash中心使用指南-文章-id=145操作")
        return self.click_element(loc.help_art_loc_2_2,"帮助中心页面-Flash中心使用指南-文章-id=145")

    def click_art_3(self):
        logger.info("开始进行：点击帮助中心页面-Flash中心使用指南-文章-id=146操作")
        return self.click_element(loc.help_art_loc_2_3,"帮助中心页面-Flash中心使用指南-文章-id=146")

    def click_art_4(self):
        logger.info("开始进行：点击帮助中心页面-Flash中心使用指南-文章-id=147操作")
        return self.click_element(loc.help_art_loc_2_4,"帮助中心页面-Flash中心使用指南-文章-id=147")

    def click_art_5(self):
        logger.info("开始进行：点击帮助中心页面-Flash中心使用指南-文章-id=148操作")
        return self.click_element(loc.help_art_loc_2_5,"帮助中心页面-Flash中心使用指南-文章-id=148")

    def click_art_6(self):
        logger.info("开始进行：点击帮助中心页面-Flash中心使用指南-文章-id=149操作")
        return self.click_element(loc.help_art_loc_2_6,"帮助中心页面-Flash中心使用指南-文章-id=149")

    def click_art_7(self):
        logger.info("开始进行：点击帮助中心页面-Flash中心使用指南-文章-id=150操作")
        return self.click_element(loc.help_art_loc_2_7,"帮助中心页面-Flash中心使用指南-文章-id=150")

