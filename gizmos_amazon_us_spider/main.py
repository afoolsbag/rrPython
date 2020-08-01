#!/usr/bin/env python3
# coding: utf-8

"""
在 Amazon.com 美国站，按关键字搜索，爬取结果数据。

参见：https://pypi.org/project/splinter/
参见：
"""

__authod__ = 'zhengrr'
__version__ = '2020.07.31'

import selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, presence_of_element_located

us_zip_code = '20237'  # 华盛顿特区

if __name__ == '__main__':
    print('启动火狐浏览器', end='')
    tick = time.time()
    driver = webdriver.Firefox()
    print('，耗时 %.2f 秒' % (time.time() - tick))

    # 60 秒超时等待
    wait = WebDriverWait(driver, 60)

    print('访问亚马逊全球站', end='')
    tick = time.time()
    driver.get('https://www.amazon.com/')
    print('，耗时 %.2f 秒' % (time.time() - tick))

    print('变更到亚马逊美国站：')

    print('点击改变地址按钮', end='')
    tick = time.time()
    driver.find_element(By.XPATH, '//div[@id="nav-global-location-slot"]/span/a').click()
    print('，耗时 %.2f 秒' % (time.time() - tick))

    print('等待对话框弹出', end='')
    tick = time.time()
    wait.until(presence_of_element_located((By.XPATH, '//input[@id="GLUXZipUpdateInput"]')))
    print('，耗时 %.2f 秒' % (time.time() - tick))

    print('填充美国邮编', end='')
    tick = time.time()
    driver.find_element(By.XPATH, '//input[@id="GLUXZipUpdateInput"]').send_keys(us_zip_code + Keys.RETURN)
    print('，耗时 %.2f 秒' % (time.time() - tick))

    # print('提交', end='')
    # tick = time.time()
    # driver.find_element(By.XPATH, '//span[@id="GLUXZipUpdate"]//input[@type="submit"]').click()
    # print('，耗时 %.2f 秒' % (time.time() - tick))

    print('点击继续按钮', end='')
    tick = time.time()
    wait.until(element_to_be_clickable((By.XPATH, '//input[@id="GLUXConfirmClose"]')))
    print('，耗时 %.2f 秒' % (time.time() - tick))

    #    if browser.is_text_present('splinter.readthedocs.io'):
    #        print("Yes, the official website was found!")
    #    else:
    #        print("No, it wasn't found... We need to improve our SEO techniques")

    input("Press Enter to continue...")
    driver.quit()
