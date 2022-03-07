"""
!/usr/bin/python3.9
-*- coding: utf-8 -*-
@Project : Flash web UI 自动化
@Commany : 重橙网络
@Software: PyCharm
@Time    : 2022/2/25 11:48
@File    : page_conftest.py
"""
import pytest
from selenium import webdriver
from TestDatas import global_data as gd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# 实例化driver，访问登录页面
s = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
prefs = {'download.prompt_for_download': False, 'download.default_directory': r'C:\Users\Any\Downloads', }
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=options, service=s)
driver.maximize_window()
driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': r"C:\Users\2144\Downloads"}}
driver.execute("send_command", params)

# 定义testfp的fixture- 前置后置 - 作用域 - 返回值
@pytest.fixture(scope="class")
def testlogin_init():
    driver.get(gd.login_url)
    yield driver
@pytest.fixture()
def testlogin_back(testlogin_init):
    driver.get(gd.login_url)
    yield testlogin_init

# 定义testhome的fixture- 前置后置 - 作用域 - 返回值
@pytest.fixture(scope="class")
def testhome_init():
    driver.get(gd.base_url)
    yield driver
@pytest.fixture()
def testhome_back(testhome_init):
    driver.get(gd.base_url)
    yield testhome_init

# 定义testfp的fixture- 前置后置 - 作用域 - 返回值
@pytest.fixture(scope="class")
def testfp_init():
    driver.get(gd.fp_url)
    yield driver
@pytest.fixture()
def testfp_back(testfp_init):
    driver.get(gd.fp_url)
    yield testfp_init


# 定义testcs的fixture- 前置后置 - 作用域 - 返回值
@pytest.fixture(scope="class")
def testcs_init():
    driver.get(gd.cs_url)
    yield driver
@pytest.fixture()
def testcs_back(testcs_init):
    driver.get(gd.cs_url)
    yield testcs_init

# 定义testcs的fixture- 前置后置 - 作用域 - 返回值
@pytest.fixture(scope="class")
def tested_init():
    driver.get(gd.ed_url)
    yield driver
@pytest.fixture()
def tested_back(tested_init):
    driver.get(gd.ed_url)
    yield tested_init

# 定义testcs的fixture- 前置后置 - 作用域 - 返回值
@pytest.fixture(scope="class")
def testfc_init():
    driver.get(gd.fc_url)
    yield driver
@pytest.fixture()
def testfc_back(testfc_init):
    driver.get(gd.fc_url)
    yield testfc_init


# 定义testen的fixture- 前置后置 - 作用域 - 返回值
@pytest.fixture(scope="class")
def testen_init():
    driver.get(gd.en_url)
    yield driver
@pytest.fixture()
def testen_back(testen_init):
    driver.get(gd.en_url)
    yield testen_init


# 定义testen的fixture- 前置后置 - 作用域 - 返回值
@pytest.fixture(scope="class")
def testhp_init():
    driver.get(gd.hp_url)
    yield driver
@pytest.fixture()
def testhp_back(testhp_init):
    driver.get(gd.hp_url)
    yield testhp_init

# 定义testnt的fixture- 前置后置 - 作用域 - 返回值
@pytest.fixture(scope="class")
def testnt_init():
    driver.get(gd.nt_url)
    yield driver
    driver.quit()
@pytest.fixture()
def testnt_back(testnt_init):
    driver.get(gd.nt_url)
    yield testnt_init