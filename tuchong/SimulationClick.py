#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Liyd
# @Time : 2020/9/14 19:21
# @Email   : muziyadong@gmail.com
# @Software: PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
# # try:
# browser.get('https://www.12306.cn/index/')
# print(browser.current_url)
# # print(browser.get_cookies())
# # print(browser.page_source)
# # try:
# browser.implicitly_wait(10)
#
# browser.find_element_by_xpath('//*[@id="J-header-login"]/a[1]').click()
# # hand = browser.window_handles
# # print(hand)
# browser.implicitly_wait(10)
# browser.switch_to_window(browser.window_handles[-1])
# browser.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
# # browser.window_handles(browser.window_handles[-1])
# browser.find_element_by_xpath('//*[@id="J-userName"]').send_keys('12345678@qq.com')
# time.sleep(4)
# # finally:
#     # browser.close()

# try:
browser.get('http://172.20.41.116:58090/Portal/common/home.jsp')
print(browser.current_url)