#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/21 16:36
# @Author  : Susanna
# @Email   : m18818392716@163.com
# @File    : test_keywords_demo.py
# @Software: PyCharm
from selenium import webdriver

class TestKeyWords(object):
    def __init__(self,url,browser_type):
        self.driver = self.open_browser(browser_type)
        self.driver.get(url)
        # self.driver.get(url)
    # def visit(self,url):
    #     self.driver.get()

    def open_browser(self,browser_type):
        if browser_type == 'chrome':
            driver = webdriver.Chrome()
            return driver
        elif browser_type == 'firefox':
            driver = webdriver.Firefox()
            return driver
        else:
            print('type error')
    def locator(self,locator_type,value):
        if locator_type == 'xpath':
            el = self.driver.find_element_by_xpath(value)
            return el
        elif locator_type == 'id':
            el = self.driver.find_element_by_id(value)
            return el
        elif locator_type == 'name':
            el = self.driver.find_element_by_name(value)
            return el

    def action(self,action_type,locator_type,value,text):
        if action_type == 'click':
            self.locator(locator_type, value).click()
        elif action_type == 'send_keys':
            self.locator(locator_type,value).send_keys(text)
        elif action_type == 'select':
            self.locator(locator_type, value).send_keys(text)
        elif action_type == 'move':
            self.locator(locator_type, value).send_keys(text)
        elif action_type == 'quit':#关闭浏览器  释放资源
            self.driver.quit()

    def quit_browser(self):
        self.driver.quit()

if __name__ == '__main__':
    tk = TestKeyWords('http://www.baidu.com','firefox')
    tk.action('send_keys','id','kw','虚竹')
    tk.action('click', 'id', 'su', '')


