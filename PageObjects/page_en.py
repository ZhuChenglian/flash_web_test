"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 15:25
@File    : page_en.py
@Explain : 企业版页面
"""
from PageLocators.page_en_loc import EnPageLocs as loc
from Common.basepage import BasePage
from Common.my_logger import logger

class EnPage(BasePage):

    def is_exit_exist(self):
        try:
            self.wait_ele_visible(loc.exit_loc,"首页_等待退出元素可见")
        except:
            return False
        else:
            return True

    def click_en_1(self):
        logger.info("开始进行：点击企业版页面-立即咨询按钮操作")
        return self.click_element(loc.en_join_loc,"企业版页面-立即咨询按钮")

    def click_en_2(self):
        logger.info("开始进行：点击企业版页面-立即购买按钮操作")
        return self.click_element(loc.en_price_loc,"企业版页面-立即购买按钮")

    def click_en_3(self):
        logger.info("开始进行：点击企业版页面-确认购买按钮操作")
        return self.click_element(loc.en_pay_loc,"企业版页面-确认购买按钮")