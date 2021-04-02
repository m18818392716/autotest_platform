#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/21 23:29
# @Author  : Susanna
# @Email   : m18818392716@163.com
# @File    : LoginPage.py
# @Software: PyCharm

from ..base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
class LoginPage(BasePage):
    # URL
    url = 'http://ww.baidu.com'

    # 元素
    user = (By.NAME,'name')
    pwd = (By.NAME,'name')
    button = (By.XPATH,'name')

    #  业务流
    def login(self,username,password):
        self.open(self.url)
        self.input(self.user, username)
        self.input(self.pwd, password)
        self.click(self.button)

if __name__ == '__main__':
    driver = webdriver.Firefox()
    user = '11111'
    pwd = '123456'
    lp = LoginPage(driver)
    lp.login(user,pwd)