"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 11:39
@File    : page_fp_loc.py
@Explain : fp下载页面元素定位
"""
from selenium.webdriver.common.by import By

class FpPageLocs:

    # 下载按钮
    download_loc = (By.XPATH, '//a[text()="下载" and contains(@href,"latest")]')
    # ax版本下载最新版
    ax_download_loc = (By.XPATH, '//h3[text()="Adobe Flash Player ActiveX版"]/following-sibling::a[contains(@href,"latest")]')
    # pp版本下载最新版
    pp_download_loc = (By.XPATH, '//h3[text()="Adobe Flash Player PPAPI版"]/following-sibling::a[contains(@href,"latest")]')
    # np版本下载最新版
    np_download_loc = (By.XPATH, '//h3[text()="Adobe Flash Player NPAPI版"]/following-sibling::a[contains(@href,"latest")]')
    # MAC pp下载
    mac_pp_download_loc = (By.XPATH, '//em[text()="Adobe Flash Player PPAPI版"]/following-sibling::a[contains(@href,"latest")]')
    # MAC np下载
    mac_np_download_loc = (By.XPATH, '//em[text()="Adobe Flash Player NPAPI版"]/following-sibling::a[contains(@href,"latest")]')
    # 咨询客服
    customer_loc = (By.XPATH, '//a[text()="咨询客服"]')
