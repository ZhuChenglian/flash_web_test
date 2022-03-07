"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 15:25
@File    : page_fp.py
@Explain : fp页面
"""
from PageLocators.page_fp_loc import FpPageLocs as loc
from Common.basepage import BasePage
from Common.my_logger import logger

class FpPage(BasePage):

    def click_fp_1(self):
        logger.info("开始进行：点击fp页面_fc下载按钮操作")
        return self.click_element(loc.download_loc, "fp页面_fc下载按钮")

    def click_fp_2(self):
        logger.info("开始进行：点击fp页面_ax版本下载最新版操作")
        return self.click_element(loc.ax_download_loc, "fp页面_ax版本下载最新版")

    def click_fp_3(self):
        logger.info("开始进行：点击fp页面_pp版本下载最新版操作")
        return self.click_element(loc.pp_download_loc, "fp页面_pp版本下载最新版")

    def click_fp_4(self):
        logger.info("开始进行：点击fp页面_np版本下载最新版操作")
        return self.click_element(loc.np_download_loc, "fp页面_np版本下载最新版")

    def click_fp_5(self):
        logger.info("开始进行：点击fp页面_MAC pp下载操作")
        return self.click_element(loc.mac_pp_download_loc, "fp页面_MAC pp下载")

    def click_fp_6(self):
        logger.info("开始进行：点击fp页面_MAC np下载操作")
        return self.click_element(loc.mac_np_download_loc, "fp页面_MAC np下载")

    def click_fp_7(self):
        logger.info("开始进行：点击fp页面_咨询客服按钮操作")
        return self.click_element(loc.customer_loc, "fp页面_咨询客服按钮")

