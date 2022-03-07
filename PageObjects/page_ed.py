"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 15:25
@File    : page_ed.py
@Explain :教育版页面
"""
from PageLocators.page_ed_loc import EdPageLocs as loc
from Common.basepage import BasePage
from Common.my_logger import logger

class EdPage(BasePage):

    def click_ed_1(self):
        logger.info("开始进行：点击教育版页面-立即申请按钮操作")
        return self.click_element(loc.bs_contact_loc,"教育版页面-立即申请按钮")

    def click_ed_2(self):
        logger.info("开始进行：点击教育版页面-模板下载文本操作")
        return self.click_element(loc.ed_template_loc,"教育版页面-模板下载文本")

    def click_ed_3(self):
        logger.info("开始进行：点击教育版页面-进入企业版文本操作")
        return self.click_element(loc.getinto_en_loc,"教育版页面-进入企业版文本")

    def click_ed_4(self):
        logger.info("开始进行：点击教育版页面-关闭按钮操作")
        return self.click_element(loc.ep_close_loc,"教育版页面-关闭按钮")

