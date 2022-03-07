"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/3/4 11:18
@File    : basepage.py
"""
import os
import time
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from Common.my_logger import logger
from Common.handle_path import screenshot_dir


class BasePage:

    def __init__(self,driver:WebDriver):
        self.win_hans = None
        self.driver = driver

    # 等待页面元素可见
    def wait_ele_visible(self,locator,page_action,timeout=20,poll_frequency=0.5):
        """
        :param locator:元素定位
        :param page_action:页面行为，截图当中作为命名
        :param timeout: 等待超时的时间
        :param poll_frequency:
        :return:
        """
        logger.info("在 {} 行为，等待元素：{} 可见".format(page_action,locator))
        try:
            start = time.time()
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_element_located(locator))
        except:
            # 输出到日志
            logger.exception("等待元素可见失败")
            # 失败截取当前页面
            self.get_page_img(page_action)
            raise
        else:
            end = time.time()
            logger.info("等待元素可见成功，等待耗时为：{}".format(end - start))

    # 等待页面元素存在
    def wait_page_contains_element(self,locator,page_action,timeout=20,poll_frequency=0.5):
        logger.info("在 {} 行为，等待元素：{} 存在".format(page_action,locator))
        try:
            start = time.time()
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.presence_of_element_located(locator))
        except:
            # 输出到日志
            logger.exception("等待元素存在失败")
            # 失败截取当前页面
            self.get_page_img(page_action)
        else:
            end = time.time()
            logger.info("等待元素存在成功，等待耗时为：{}".format(end - start))

    # 获取元素位置，wait 默认用的是等待元素可见，如果等待的为空，则使用等待存在的元素，否则等待可见的元素
    def get_element(self,locator,page_action,timeout=20,poll_frequency=0.5,wait_exist=False):  # locator代表元素定位
        # 先等待元素可见或者存在
        if wait_exist is False:  # if wait是None，是False
            self.wait_page_contains_element(locator,page_action,timeout,poll_frequency)
        else:
            self.wait_ele_visible(locator,page_action)
        # 元素等待或者存在
        logger.info("在 {} 行为，查找元素：{}".format(page_action,locator))
        try:
            ele = self.driver.find_element(*locator)
        except:
            # 输出日志
            logger.exception("查找元素失败")
            # 失败截取当前页面
            self.get_page_img(page_action)
            raise
        else:
            return ele

    # 点击元素操作
    def click_element(self,locator,page_action,timeout=20,poll_frequency=0.5):
        # 等待- 查找
        ele = self.get_element(locator,page_action,timeout,poll_frequency)
        # 点击
        logger.info("在 {} 行为，点击元素：{}".format(page_action,locator))
        try:
            ActionChains(self.driver).move_to_element(ele).perform()
            sleep(1)
            ActionChains(self.driver).click(ele).perform()
            # 判断是否是下载链接，如果是，则等待2s，下载完成，如果不是，则不等待
            if locator[1].find("latest"):
                sleep(2)
            else:
                pass
        except:
            logger.exception("点击操作失败")
            self.get_page_img(page_action)
            raise

    # 输入文本内容
    def input_text(self,locator,page_action,value,timeout=20,poll_frequency=0.5):
        # 等待- 查找
        ele = self.get_element(locator,page_action,timeout,poll_frequency)
        logger.info("在 {} 行为，给元素：{} 输入文本值: {}".format(page_action,locator,value))
        try:
            ele.clear()
            ele.send_keys(value)
        except:
            logger.exception("元素输入文本失败")
            self.get_page_img(page_action)
            raise

    # 等待元素存在，并获取元素文本
    def get_text(self,locator,page_action,timeout=20,poll_frequency=0.5):
        ele = self.get_element(locator,page_action,timeout,poll_frequency,wait_exist=True)
        logger.info("在 {} 行为，获取元素 {} 的文本值".format(page_action,locator))
        try:
            txt = ele.text
        except:
            logger.exception("获取元素文本失败")
            self.get_page_img(page_action)
            raise
        else:
            logger.info("文本值为：{}".format(txt))
            return txt

    # 获取元素属性
    def get_attribute(self,locator,page_action,attr,timeout=20,poll_frequency=0.5):
        ele = self.get_element(locator,page_action,timeout,poll_frequency,wait_exist=True)
        logger.info("在 {} 行为，获取元素 {} 的属性值".format(page_action,locator))
        try:
            value = ele.get_attribute(attr)
        except:
            logger.exception("获取元素属性失败")
            self.get_page_img(page_action)
            raise
        else:
            logger.info("属性值为：{}".format(value))
            return value

    # 切换到新窗口，并关闭新窗口
    def switch_and_close_window(self):
        # 获取所有的窗口句柄
        self.win_hans = self.driver.window_handles
        if len(self.win_hans) > 1:
            self.driver.switch_to.window(self.win_hans[-1])
            logger.info("获取最新窗口句柄：{}，并切换到新窗口".format(self.win_hans[-1]))
            self.driver.close()
            logger.info("关闭当前窗口页面")
        else:
            # 如果等于1，则切换到当前唯一的窗口
            self.driver.switch_to.window(self.win_hans[-1])
            logger.info("获取最新窗口句柄: {}，并切换到新窗口".format(self.win_hans[-1]))

    # 切换到新窗口
    def switch_window(self):
        self.win_hans = self.driver.window_handles
        self.driver.switch_to.window(self.win_hans[-1])

    # 关闭当前窗口
    def close_cur_window(self):
        self.driver.close()

    # 获取错误截图
    def get_page_img(self,page_action):
        # 命名规范：{XX页面__XX操作}__截图时间.png
        cur_time = time.strftime('%Y年%m月%d日 %H时%M分%S秒',time.localtime())
        file_path = os.path.join(screenshot_dir,"{}_{}.png".format(page_action,cur_time))
        self.driver.save_screenshot(file_path)
        logger.info("截图保存在：{}".format(file_path))
