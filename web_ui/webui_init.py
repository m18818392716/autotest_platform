#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/21 20:28
# @Author  : Susanna
# @Email   : m18818392716@163.com
# @File    : webui_init.py
# @Software: PyCharm

from selenium import webdriver
from time import sleep
import json
import jsonpath
import requests

class WebUI_Framework(object):
    # 创建日志对象
    # log = Logger().get_logger()

    # 初始换WebUI_init类
    def __init__(self,url,browser_type):
        self.driver = self.open_browser(browser_type)
        self.driver.get(url)

    def visit(self,**kwargs):
        self.driver.get(kwargs['txt'])
    #   关闭浏览器
    def quit(self,**kwargs):
        self.driver.quit()

    def open_browser(self,browser_type):
        if browser_type == 'chrome':
            driver = webdriver.Chrome()
            return driver
        elif browser_type == 'firefox':
            driver = webdriver.Firefox()
            return driver
        else:
            print('type error')

    def locator(self,By,**kwargs):
        try:
            return self.driver.find_element(getattr(By,kwargs['loc'].upper()),kwargs['txt'])
        except Exception as e:
            print('元素定位失败，信息：{0}'.format(e))

    # 根据不同的定位方法，进行点击操作
    def click(self,**kwargs):
        self.locator(**kwargs).click()
    # 根据不同的定位方法，进行输入操作
    def input(self,**kwargs):
        self.locator(**kwargs).send_keys(kwargs['txt'])
    # 定义强制等待
    def sleep(self,**kwargs):
        sleep(kwargs['txt'])

    # 定义隐式等待
    def wait(self,**kwargs):
        self.driver.implicitly_wait(kwargs['txt'])

    def switch_and_close(self, **kwargs):
        handles = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to_window(handles[1])

    #     切换至Iframe窗体
    def switch_to_iframe(self,**kwargs):
        self.driver.switch_to_frame(self.locator(**kwargs))

    #     切换至more窗体
    def switch_to_default(self, **kwargs):
        self.driver.switch_to_default_content()


    def get(self,url, headers = None, param = None):
        # if param is not None:
        #     data = self.json_dumps(param)
        return requests.get(url, headers=headers, params=param)

    def post(self,url, headers = None, data = None):
        if data is not None:
            data = self.json_dumps(data)
        return requests.get(url, headers=headers, data=data)

    def json_dumps(self,data):
        try:
            return json.dumps(data)
        except Exception as e:
            return e

    def get_msg(self,res,key):
        if res is not None:
            try:
                txt = json.loads(res)
                value = jsonpath.jsonpath(txt,'$..{0}'.format(key))
                if value:
                    if len(value) == 1:
                        return value[0]
                return value
            except Exception as e:
                return e
        else:
            return None



