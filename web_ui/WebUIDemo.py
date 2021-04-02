#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/21 15:57
# @Author  : Susanna
# @Email   : m18818392716@163.com
# @File    : WebUIDemo.py
# @Software: PyCharm

'''
    1、Selenium运行机制
   selenium中所有的操作都是基于webdriver来实现的
   2、创建浏览器
   3、输入搜索条件
   4、点击搜索按钮
   5、关闭浏览器
   线性代码不能转弯   没有任何可以被优化或者复用或者产生价值的东西
'''
from time import sleep

# 基于selenium来生成driver对象，所以需要导入selenium模块
from selenium import webdriver

# 生成一个ChromeDriver  一定记得加()
driver = webdriver.Firefox()
# 访问指定的url
driver.get('http://www.baidu.com')
input = driver.find_element('id','kw')
input.send_keys("Python")
button = driver.find_element('id','su')
button.click()


# driver.find_element_by_id("kw").send_keys("Python")
# driver.find_element_by_id("su").click()

# 等待
sleep(2)


# 点击第一条链接
# driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[3]/div[1]/h3/a[1]").click()

# 关闭浏览器
driver.quit()

# 点击第二条链接
