"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 11:40
@File    : page_hp_loc.py
@Explain : 帮助中心页面元素定位
"""
from selenium.webdriver.common.by import By

class HpPageLocs:

    # 安装与更新问题
    help_data_loc_1 = (By.XPATH, '//li[@data-id="1"]')
    help_art_loc_1_1 = (By.XPATH,'//a[contains(@href,"id=16")]')
    help_art_loc_1_2 = (By.XPATH,'//a[contains(@href,"id=62")]')
    help_art_loc_1_3 = (By.XPATH,'//a[contains(@href,"id=63")]')
    help_art_loc_1_4 = (By.XPATH,'//a[contains(@href,"id=64")]')
    help_art_loc_1_5 = (By.XPATH,'//a[contains(@href,"id=68")]')
    help_art_loc_1_6 = (By.XPATH,'//a[contains(@href,"id=111")]')
    help_art_loc_1_7 = (By.XPATH,'//a[contains(@href,"id=112")]')
    help_art_loc_1_8 = (By.XPATH,'//a[contains(@href,"id=113")]')

    # Flash中心使用指南
    help_data_loc_2 = (By.XPATH,'//li[@data-id="2"]')
    help_art_loc_2_1 = (By.XPATH,'//a[contains(@href,"id=142")]')
    help_art_loc_2_2 = (By.XPATH,'//a[contains(@href,"id=145")]')
    help_art_loc_2_3 = (By.XPATH,'//a[contains(@href,"id=146")]')
    help_art_loc_2_4 = (By.XPATH,'//a[contains(@href,"id=147")]')
    help_art_loc_2_5 = (By.XPATH,'//a[contains(@href,"id=148")]')
    help_art_loc_2_6 = (By.XPATH,'//a[contains(@href,"id=149")]')
    help_art_loc_2_7 = (By.XPATH,'//a[contains(@href,"id=150")]')

    # Flash运行异常
    help_data_loc_3 = (By.XPATH,'//li[@data-id="3"]')
    help_art_loc_3_1 = (By.XPATH,'//a[contains(@href,"id=31")]')
    help_art_loc_3_2 = (By.XPATH,'//a[contains(@href,"id=33")]')
    help_art_loc_3_3 = (By.XPATH,'//a[contains(@href,"id=55")]')
    help_art_loc_3_4 = (By.XPATH,'//a[contains(@href,"id=61")]')
    help_art_loc_3_5 = (By.XPATH,'//a[contains(@href,"id=66")]')
    help_art_loc_3_6 = (By.XPATH,'//a[contains(@href,"id=67")]')
    help_art_loc_3_7 = (By.XPATH,'//a[contains(@href,"id=68")]')
    help_art_loc_3_8 = (By.XPATH,'//a[contains(@href,"id=109")]')
    help_art_loc_3_9 = (By.XPATH,'//a[contains(@href,"id=115")]')
    help_art_loc_3_10 = (By.XPATH,'//a[contains(@href,"id=125")]')
    help_art_loc_3_11 = (By.XPATH,'//a[contains(@href,"id=127")]')
    help_art_loc_3_12 = (By.XPATH,'//a[contains(@href,"id=156")]')
    help_art_loc_3_13 = (By.XPATH,'//a[contains(@href,"id=159")]')

    # 版本问题
    help_data_loc_4 = (By.XPATH,'//li[@data-id="4"]')
    help_art_loc_4_1 = (By.XPATH,'//a[contains(@href,"id=167")]')
    help_art_loc_4_2 = (By.XPATH,'//a[contains(@href,"id=166")]')
    help_art_loc_4_3 = (By.XPATH,'//a[contains(@href,"id=168")]')
    help_art_loc_4_4 = (By.XPATH,'//a[contains(@href,"id=31")]')
    help_art_loc_4_5 = (By.XPATH,'//a[contains(@href,"id=61")]')
    help_art_loc_4_6 = (By.XPATH,'//a[contains(@href,"id=66")]')
    help_art_loc_4_7 = (By.XPATH,'//a[contains(@href,"id=169")]')

    # 常见问题
    help_data_loc_5 = (By.XPATH,'//li[@data-id="5"]')
    help_art_loc_5_1 = (By.XPATH,'//a[contains(@href,"id=16")]')
    help_art_loc_5_2 = (By.XPATH,'//a[contains(@href,"id=55")]')
    help_art_loc_5_3 = (By.XPATH,'//a[contains(@href,"id=62")]')
    help_art_loc_5_4 = (By.XPATH,'//a[contains(@href,"id=63")]')
    help_art_loc_5_5 = (By.XPATH,'//a[contains(@href,"id=64")]')
    help_art_loc_5_6 = (By.XPATH,'//a[contains(@href,"id=67")]')
    help_art_loc_5_7 = (By.XPATH,'//a[contains(@href,"id=68")]')
    help_art_loc_5_8 = (By.XPATH,'//a[contains(@href,"id=115")]')
    help_art_loc_5_9 = (By.XPATH,'//a[contains(@href,"id=175")]')

    # Flash不可用问题
    help_data_loc_10 = (By.XPATH,'//li[@data-id="10"]')
    help_art_loc_10_1 = (By.XPATH,'//a[contains(@href,"id=61")]')
    help_art_loc_10_2 = (By.XPATH,'//a[contains(@href,"id=62")]')
    help_art_loc_10_3 = (By.XPATH,'//a[contains(@href,"id=64")]')
    help_art_loc_10_4 = (By.XPATH,'//a[contains(@href,"id=66")]')
    help_art_loc_10_5 = (By.XPATH,'//a[contains(@href,"id=68")]')
    help_art_loc_10_6 = (By.XPATH,'//a[contains(@href,"id=115")]')
    help_art_loc_10_7 = (By.XPATH,'//a[contains(@href,"id=148")]')
