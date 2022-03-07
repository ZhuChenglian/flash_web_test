"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 11:40
@File    : page_nt_loc.py
@Explain : N官方公告页面元素定位
"""
from selenium.webdriver.common.by import By

class NtPageLocs:

    # 文章元素定位
    notice_art_loc_1 = (By.XPATH,'//a[contains(@href,"id=178")]')
    notice_art_loc_2 = (By.XPATH,'//a[contains(@href,"id=177")]')
    notice_art_loc_3 = (By.XPATH,'//a[contains(@href,"id=173")]')
    notice_art_loc_4 = (By.XPATH,'//a[contains(@href,"id=170")]')
    notice_art_loc_5 = (By.XPATH,'//a[contains(@href,"id=157")]')
    notice_art_loc_6 = (By.XPATH,'//a[contains(@href,"id=154")]')
    notice_art_loc_7 = (By.XPATH,'//a[contains(@href,"id=153")]')
    notice_art_loc_8 = (By.XPATH,'//a[contains(@href,"id=144")]')
    notice_art_loc_9 = (By.XPATH,'//a[contains(@href,"id=143")]')
    notice_art_loc_10 = (By.XPATH,'//a[contains(@href,"id=140")]')
    notice_art_loc_11 = (By.XPATH,'//a[contains(@href,"id=138")]')
