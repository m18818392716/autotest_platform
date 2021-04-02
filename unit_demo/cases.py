#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/21 21:38
# @Author  : Susanna
# @Email   : m18818392716@163.com
# @File    : cases.py
# @Software: PyCharm
import unittest
from time import sleep
from selenium import webdriver
from ddt import ddt,data,unpack,file_data

@ddt
class Cases(unittest.TestCase):
    # 前置条件
    def setUp(self):
        print('setUp方法')
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.baidu.com')

    # 后置条件
    def tearDown(self):
        print('tearDown方法')
        self.driver.quit()

    # 定义测试用例  必须以test开头的函数才可以能够被识别为测试用例

    '''
    @data解析是将内容依照,来进行解析
    '''
    # @data(['id','Python'],['id','王俊凯'],['id','刘一刀'])
    # @unpack
    @file_data('../data/user.yaml')
    def test_01(self,locator,keyword):
        print('这是一条测试用例1')
        self.driver.find_element(locator, 'kw').send_keys(keyword)
        self.driver.find_element('id', 'su').click()
        sleep(3)
        self.demo()


    def demo(self):
        print('这是demo')

    # def test_03(self):
    #     print('这是一条测试用例3')
    #     self.driver.find_element('id', 'kw').send_keys("虚竹")
    #     self.driver.find_element('id', 'su').click()
    #     sleep(3)
    #     self.demo()
    #
    # def test_02(self):
    #     print('这是一条测试用例2')
    #     self.driver.find_element('id', 'kw').send_keys("龚俊")
    #     self.driver.find_element('id', 'su').click()
    #     sleep(3)
    #     self.demo()

    @file_data('../data/user.yaml')
    def test_04(self, **kwargs):
        print(kwargs['locator'])
        print(kwargs['keyword'])
        self.assertEqual('id111',kwargs['locator'],msg='断言失败')


#         Unittest的执行  必须通过main函数调用unittest.main()函数来执行
if __name__ == '__main__':
    unittest.main()
