"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 15:25
@File    : page_hp_3.py
@Explain : 帮助中心页面
"""
from time import sleep
from PageLocators.page_hp_loc import HpPageLocs as loc
from Common.basepage import BasePage
from Common.my_logger import logger

class HpPage_3(BasePage):

    def click_help_data_3(self):
        logger.info("开始进行：点击帮助中心页面-Flash运行异常文本操作")
        return self.click_element(loc.help_data_loc_3,"帮助中心页面-Flash运行异常文本")

    def click_art_1(self):
        logger.info("开始进行：点击帮助中心页面-Flash运行异常-文章-id=31操作")
        return self.click_element(loc.help_art_loc_3_1,"帮助中心页面-Flash运行异常-文章-id=31")

    def click_art_2(self):
        logger.info("开始进行：点击帮助中心页面-Flash运行异常-文章-id=33操作")
        return self.click_element(loc.help_art_loc_3_2,"帮助中心页面-Flash运行异常-文章-id=33")

    def click_art_3(self):
        logger.info("开始进行：点击帮助中心页面-Flash运行异常-文章-id=55操作")
        return self.click_element(loc.help_art_loc_3_3,"帮助中心页面-Flash运行异常-文章-id=55")

    def click_art_4(self):
        logger.info("开始进行：点击帮助中心页面-Flash运行异常-文章-id=61操作")
        return self.click_element(loc.help_art_loc_3_4,"帮助中心页面-Flash运行异常-文章-id=61")

    def click_art_5(self):
        logger.info("开始进行：点击帮助中心页面-Flash运行异常-文章-id=66操作")
        return self.click_element(loc.help_art_loc_3_5,"帮助中心页面-Flash运行异常-文章-id=66")

    def click_art_6(self):
        logger.info("开始进行：点击帮助中心页面-Flash运行异常-文章-id=67操作")
        return self.click_element(loc.help_art_loc_3_6,"帮助中心页面-Flash运行异常-文章-id=67")

    def click_art_7(self):
        logger.info("开始进行：点击帮助中心页面-Flash运行异常-文章-id=68操作")
        return self.click_element(loc.help_art_loc_3_7,"帮助中心页面-Flash运行异常-文章-id=69")

    def click_art_8(self):
        logger.info("开始进行：点击帮助中心页面-Flash运行异常-文章-id=109操作")
        return self.click_element(loc.help_art_loc_3_8,"帮助中心页面-Flash运行异常-文章-id=109")
    def click_art_9(self):
        logger.info("开始进行：点击帮助中心页面-Flash运行异常-文章-id=115操作")
        return self.click_element(loc.help_art_loc_3_9,"帮助中心页面-Flash运行异常-文章-id=115")

    def click_art_10(self):
        logger.info("开始进行：点击帮助中心页面-Flash运行异常-文章-id=125操作")
        return self.click_element(loc.help_art_loc_3_10,"帮助中心页面-Flash运行异常-文章-id=125")

    def click_art_11(self):
        logger.info("开始进行：点击帮助中心页面-Flash运行异常-文章-id=127操作")
        return self.click_element(loc.help_art_loc_3_11,"帮助中心页面-Flash运行异常-文章-id=127")

    def click_art_12(self):
        logger.info("开始进行：点击帮助中心页面-Flash运行异常-文章-id=156操作")
        return self.click_element(loc.help_art_loc_3_12,"帮助中心页面-Flash运行异常-文章-id=156")

    def click_art_13(self):
        logger.info("开始进行：点击帮助中心页面-Flash运行异常-文章-id=159操作")
        return self.click_element(loc.help_art_loc_3_13,"帮助中心页面-Flash运行异常-文章-id=159")