"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 13:55
@File    : page_fc_loc.py
@Explain : fc页面元素定位
"""
from selenium.webdriver.common.by import By

class FcPageLocs:

    # 上方立即体验按钮
    fc_top_download_loc = (By.XPATH,'//div[@id="lobby-download"]/a[contains(@href,"latest")]')
    # 下方立即体验按钮
    fc_low_download_loc = (By.XPATH,'//div[@id="lobby-download2"]/a[contains(@href,"latest")]')

