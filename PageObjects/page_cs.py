"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 15:24
@File    : page_cs.py
@Explain :客服支持页面
"""
from PageLocators.page_cs_loc import CsPageLocs as loc
from Common.basepage import BasePage
from Common.my_logger import logger

class CsPage(BasePage):

    def click_cs_1(self):
        logger.info("开始进行：点击客服支持页面-客服支持按钮操作")
        return self.click_element(loc.bs_qq_loc, "客服支持页面-客服支持按钮")

    def click_cs_2(self):
        logger.info("开始进行：点击客服支持页面-弹窗-文章-id=125操作")
        return self.click_element(loc.cs_art_loc_1, "客服支持页面-弹窗-文章-id=125")

    def click_cs_3(self):
        logger.info("开始进行：点击客服支持页面-弹窗-文章-id=16操作")
        return self.click_element(loc.cs_art_loc_2, "客服支持页面-弹窗-文章-id=16")

    def click_cs_4(self):
        logger.info("开始进行：点击客服支持页面-弹窗-文章-id=63操作")
        return self.click_element(loc.cs_art_loc_3, "客服支持页面-弹窗-文章-id=63")

    def click_cs_5(self):
        logger.info("开始进行：点击客服支持页面-弹窗-文章-id=31操作")
        return self.click_element(loc.cs_art_loc_4, "客服支持页面-弹窗-文章-id=31")

    def click_cs_6(self):
        logger.info("开始进行：点击客服支持页面-联系客服按钮操作")
        return self.click_element(loc.cs_pop_btn_loc, "客服支持页面-联系客服按钮")

    def click_cs_7(self):
        logger.info("开始进行：点击客服支持页面-弹窗关闭按钮操作")
        return self.click_element(loc.bs_qq_close_loc, "客服支持页面-弹窗关闭按钮")

    def click_cs_8(self):
        logger.info("开始进行：点击客服支持页面-文章-id=16操作")
        return self.click_element(loc.qs_art_loc_1, "客服支持页面-文章-id=16")

    def click_cs_9(self):
        logger.info("开始进行：点击客服支持页面-文章-id=55操作")
        return self.click_element(loc.qs_art_loc_2, "客服支持页面-文章-id=55")

    def click_cs_10(self):
        logger.info("开始进行：点击客服支持页面-文章-id=62操作")
        return self.click_element(loc.qs_art_loc_3, "客服支持页面-文章-id=62")

    def click_cs_11(self):
        logger.info("开始进行：点击客服支持页面-文章-id=63操作")
        return self.click_element(loc.qs_art_loc_4, "客服支持页面-文章-id=63")

    def click_cs_12(self):
        logger.info("开始进行：点击客服支持页面-文章-id=64操作")
        return self.click_element(loc.qs_art_loc_5, "客服支持页面-文章-id=64")

    def click_cs_13(self):
        logger.info("开始进行：点击客服支持页面-文章-id=67操作")
        return self.click_element(loc.qs_art_loc_6, "客服支持页面-文章-id=67")

