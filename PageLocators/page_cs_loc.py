"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 11:40
@File    : page_cs_loc.py
@Explain : 客服支持页面元素定位
"""
from selenium.webdriver.common.by import By

class CsPageLocs:

    # 客服支持按钮
    bs_qq_loc = (By.XPATH,'//a[@class="bs-qq"]')

    # 弹框中元素定位
    # 文章
    cs_art_loc_1 = (By.XPATH,'//ul[@class="online-service-pop-question"]/li/a[contains(@href,"id=125")]')
    cs_art_loc_2 = (By.XPATH,'//ul[@class="online-service-pop-question"]/li/a[contains(@href,"id=16")]')
    cs_art_loc_3 = (By.XPATH,'//ul[@class="online-service-pop-question"]/li/a[contains(@href,"id=63")]')
    cs_art_loc_4 = (By.XPATH,'//ul[@class="online-service-pop-question"]/li/a[contains(@href,"id=31")]')
    # 联系客服按钮
    cs_pop_btn_loc = (By.XPATH,'//div[@class="online-service-pop-list"]/a[@class="online-service-pop-btn"]')
    # 关闭按钮
    bs_qq_close_loc = (By.XPATH,'//i[@class="online-service-pop-close"]')

    # 文章
    qs_art_loc_1 = (By.XPATH,'//a[contains(@href,"id=16")]')
    qs_art_loc_2 = (By.XPATH,'//a[contains(@href,"id=55")]')
    qs_art_loc_3 = (By.XPATH,'//a[contains(@href,"id=62")]')
    qs_art_loc_4 = (By.XPATH,'//a[contains(@href,"id=63")]')
    qs_art_loc_5 = (By.XPATH,'//a[contains(@href,"id=64")]')
    qs_art_loc_6 = (By.XPATH,'//a[contains(@href,"id=67")]')
