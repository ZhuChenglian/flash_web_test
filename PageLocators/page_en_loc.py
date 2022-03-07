"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 11:39
@File    : page_en_loc.py
@Explain : 企业版页面元素定位
"""
from selenium.webdriver.common.by import By

class EnPageLocs:

    # 退出按钮
    exit_loc = (By.XPATH, '//a[@class="top-user-logout"]')
    # 立即咨询按钮
    en_join_loc = (By.XPATH,'//a[@class="en-join-top"]')
    # 立即购买按钮
    en_price_loc = (By.XPATH,'//div[@class="en-price-button"]')
    # 确认购买按钮
    en_pay_loc = (By.XPATH,'//div[@class="en-pay-button"]')