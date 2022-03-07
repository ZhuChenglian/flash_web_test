"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 11:39
@File    : page_home_loc.py
@Explain : 首页页面元素定位
"""
from selenium.webdriver.common.by import By

class HomePageLocs:

    # 立即下载按钮
    fc_download_loc = (By.XPATH, '//a[contains(@href,"latest")]')
    # Adobe Flash Player下载 文本点击
    fp_download_loc = (By.XPATH, '//a[text()="Adobe Flash Player下载"]')
    # 企业版链接跳转
    ep_download_loc = (By.XPATH, '//a[text()="企业版授权下载"]')
    # 首页
    home_loc = (By.XPATH, '//a[text()="首页"]')
    # flash中心
    flash_center_loc = (By.XPATH, '//a[text()="Flash中心"]')
    # 企业版
    enterprise_loc = (By.XPATH, '//a[text()="企业版"]')
    # 教育版
    education_loc = (By.XPATH, '//a[text()="教育版"]')
    # 帮助中心
    help_center_loc = (By.XPATH, '//a[text()="帮助中心"]')
    # 客服支持
    custom_service_loc = (By.XPATH, '//a[text()="客服支持"]')
    # 官方公告
    notice_item_loc = (By.XPATH, '//a[text()="官方公告"]')
