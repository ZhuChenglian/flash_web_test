"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 15:53
@File    : page_common.py
"""
from Common.basepage import BasePage
from Common.my_logger import logger

class CommonPage(BasePage):

    # 返回上一页
    def back_last_page(self):
        logger.info("开始进行：返回上一个页面操作")
        return self.driver.back()

    # 切换到新窗口并关闭窗口
    def close_switch_window(self):
        return self.switch_and_close_window()

    # 切换到新窗口，不关闭
    def switch_window_no_close(self):
        return self.switch_window()

    # 关闭当前窗口
    def close_window(self):
        return self.close_cur_window()