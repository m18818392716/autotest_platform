#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/21 23:21
# @Author  : Susanna
# @Email   : m18818392716@163.com
# @File    : base_page.py
# @Software: PyCharm

from selenium import webdriver
class BasePage:
    # 构造函数
    def __init__(self,driver):
        self.driver = driver

    def open(self,url):
        self.driver.get(url)

    def locator(self,loc):
        return self.driver.find_element(*loc)

    def input(self,loc,txt):
        self.locator(loc).send_keys(txt)

    def click(self,loc):
        self.locator(loc).click()