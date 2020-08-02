#!/usr/bin/env python3
# coding: utf-8

"""
在 Amazon.com 美国站，按关键字搜索，爬取结果数据。

参见：https://pypi.org/project/selenium/
"""

__version__ = '2020.08.02'
__since__ = '2020.07.31'
__author__ = 'zhengrr'
__license__ = 'Unlicense'

from dataclasses import dataclass
from datetime import datetime
from random import randint
from time import sleep
from time import time
from typing import Optional

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.expected_conditions import presence_of_element_located

# 搜索配置
US_ZIP_CODE: str = '20237'  # 搜索地邮编，如 20237 为华盛顿特区
SEARCH_KEYS: str = 'face mask'  # 搜索关键字
MAX_COUNT: int = 200  # 抓取结果的最大数量


@dataclass
class Data:
    asin: Optional[str] = None
    title: Optional[str] = None
    price: Optional[str] = None
    image: Optional[str] = None


if __name__ == '__main__' or True:
    first_line_time = time()

    # --------------------------------------------------------------------------
    # 启动火狐浏览器

    print('启动火狐浏览器', end='')
    tick = time()
    driver = webdriver.Firefox()
    print('，耗时 %.2f 秒' % (time() - tick))

    # 10 秒超时等待
    wait = WebDriverWait(driver, 10)

    # 随机休眠 0.5 ~ 2.0 秒
    random_sleep = lambda: sleep(randint(500, 2000) / 1000.0)

    # --------------------------------------------------------------------------
    # 访问亚马逊全球站

    print('访问亚马逊全球站', end='')
    tick = time()
    driver.get('https://www.amazon.com/')
    print('，耗时 %.2f 秒' % (time() - tick))

    # --------------------------------------------------------------------------
    # 变更到亚马逊美国站

    print('\n变更到亚马逊美国站：')

    print('点击改变地址按钮', end='')
    tick = time()
    driver.find_element(By.XPATH, '//div[@id="nav-global-location-slot"]/span/a').click()
    print('，耗时 %.2f 秒' % (time() - tick))

    print('等待对话框弹出', end='')
    tick = time()
    edt = wait.until(presence_of_element_located((By.ID, 'GLUXZipUpdateInput')))
    print('，耗时 %.2f 秒' % (time() - tick))

    random_sleep()

    print('填充美国邮编并提交', end='')
    tick = time()
    edt.send_keys(US_ZIP_CODE + Keys.RETURN)
    print('，耗时 %.2f 秒' % (time() - tick))

    # 在上一步使用回车键提交，不使用鼠标点击提交
    # print('提交', end='')
    # tick = time.time()
    # driver.find_element(By.XPATH, '//span[@id="GLUXZipUpdate"]//input[@type="submit"]').click()
    # print('，耗时 %.2f 秒' % (time.time() - tick))

    random_sleep()

    print('点击继续按钮', end='')
    tick = time()
    try:
        btn = wait.until(element_to_be_clickable((By.ID, 'GLUXConfirmClose')))
        btn.click()
    except TimeoutException:
        ActionChains(driver).move_by_offset(813, 644).click().perform()
    print('，耗时 %.2f 秒' % (time() - tick))

    random_sleep()

    # --------------------------------------------------------------------------
    # 搜索

    print('\n搜索：')

    print('等待页面加载完毕', end='')
    tick = time()
    while True:
        try:
            edt = wait.until(presence_of_element_located((By.ID, 'twotabsearchtextbox')))
            break
        except StaleElementReferenceException:
            pass
    print('，耗时 %.2f 秒' % (time() - tick))

    random_sleep()

    print('填充搜索关键字并提交', end='')
    tick = time()
    while True:
        try:
            edt = wait.until(presence_of_element_located((By.ID, 'twotabsearchtextbox')))
            edt.send_keys(SEARCH_KEYS + Keys.RETURN)
            break
        except StaleElementReferenceException:
            pass
    print('，耗时 %.2f 秒' % (time() - tick))

    # --------------------------------------------------------------------------
    # 抓取搜索结果

    print('\n抓取搜索结果：')

    data_list: list = []
    while True:
        print('等待页面加载完毕', end='')
        tick = time()
        wait.until(presence_of_element_located((By.XPATH, '//div[@data-asin][@data-index="2"][@data-uuid]')))
        sleep(3)  # 额外等 3 秒，让其余项加载完毕
        print('，耗时 %.2f 秒' % (time() - tick))

        divs = driver.find_elements(By.XPATH, '//div[@data-asin]')
        print('本页粗略找到 %i 个结果项' % len(divs))

        for div in divs:
            try:
                data = Data()
                data.asin = div.get_attribute('data-asin')
                if not data.asin:
                    continue
                data.title = div.find_element(By.XPATH, './/h2//span').text
                if not data.title:
                    continue
                data.price = div.find_element(By.XPATH, './/span[@class="a-price"]/span[@class="a-offscreen"]') \
                    .get_attribute('textContent')
                if not data.price:
                    continue
                data.image = div.find_element(By.XPATH, './/span[@data-component-type="s-product-image"]//img') \
                    .get_attribute('src')
                if not data.image:
                    continue
                data_list.append(data)
            except NoSuchElementException:
                continue

        if len(data_list) < MAX_COUNT:
            next_btn = wait.until(
                element_to_be_clickable((By.XPATH, '//ul[@class="a-pagination"]//li[@class="a-last"]//a')))
            next_btn.click()
            continue
        else:
            break

    now_time = datetime.now().replace(microsecond=0).isoformat()
    file_name = ('%s %s.csv' % (now_time, SEARCH_KEYS)).replace(':', '-').replace(' ', '_')
    file = open(file_name, 'w', encoding='utf-16-be')
    file.write('"ASIN","TITLE","PRICE","IMAGE"\n')
    for data in data_list:
        file.write('"%s","%s","%s","%s"\n' % (data.asin, data.title, data.price, data.image))

    # input('Press Enter to continue...')
    driver.quit()

    # --------------------------------------------------------------------------
    # 小结

    print('\n小结：')

    print('总计找到 %i 项结果' % len(data_list))
    print('结果存储到 %s 文件' % file_name)
    print('总耗时 %.2f 秒' % (time() - first_line_time))
