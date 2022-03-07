"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 15:25
@File    : page_fc.py
@Explain : fc页面
"""
from PageLocators.page_fc_loc import FcPageLocs as loc
from Common.basepage import BasePage
from Common.my_logger import logger

class FcPage(BasePage):

    def click_fc_1(self):
        logger.info("开始进行：点击fc页面_上方立即体验按钮操作")
        return self.click_element(loc.fc_top_download_loc, "fc页面_上方立即体验按钮")

    def click_fc_2(self):
        logger.info("开始进行：点击fc页面_下方立即体验按钮操作")
        return self.click_element(loc.fc_low_download_loc, "fc页面_下方立即体验按钮")
