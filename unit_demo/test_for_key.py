#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/21 17:36
# @Author  : Susanna
# @Email   : m18818392716@163.com
# @File    : test_for_key.py
# @Software: PyCharm

import unittest
from time import sleep
from web_ui.test_keywords_demo import TestKeyWords
from ddt import ddt,data,unpack

@ddt
class TestForKey(unittest.TestCase):
    # 前置条件
    def setUp(self) -> None:
        self.tk = TestKeyWords('http://www.baidu.com', 'firefox')
    # 后置条件
    def tearDown(self) -> None:
        self.tk.quit_browser()
    # 测试用例1
    @data(['id','虚竹'],['id','龚俊'])
    @unpack
    def test_1(self,locator,input_value):
        self.tk.action('send_keys', locator, 'kw', input_value)
        self.tk.action('click', 'id', 'su', '')
        sleep(3)
    #   测试用例2
    # def test_2(self):
    #     self.tk.action('send_keys', 'id', 'kw', '龚俊')
    #     self.tk.action('click', 'id', 'su', '')
    #     sleep(3)

if __name__ == '__main__':
    unittest.main()
