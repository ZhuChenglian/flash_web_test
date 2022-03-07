"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 11:39
@File    : page_ed_loc.py
@Explain : 教育版页面元素定位
"""
from selenium.webdriver.common.by import By

class EdPageLocs:

    # 立即申请按钮
    bs_contact_loc = (By.XPATH,'//a[@class="bs-contact"]')
    # 模板下载文本元素
    ed_template_loc = (By.XPATH,'//a[text()="模板点击下载"]')
    # 进入企业版文本元素
    getinto_en_loc = (By.XPATH,'//a[text()="点击进入企业版"]')
    # 关闭按钮
    ep_close_loc = (By.XPATH,'//i[@class="ep-close"]')
