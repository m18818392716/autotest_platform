#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/20 22:16
# @Author  : Susanna
# @Email   : m18818392716@163.com
# @File    : test.py
# @Software: PyCharm

str = "this is string example....wow!!!"
print (str.startswith( 'this' ))
print (str.startswith( 'string', 8 ))
print (str.startswith( 'i', 2, 3 ))
print (str.endswith( '!!!' ))
print (str.endswith( 'h', 0, 1 ))

import requests,unittest
import json

class RunMain(object):

    def send_get(self, url, headers,data):
        res = requests.get(url=url,params=headers,data=data).json()
        return res

    def send_post(self, url, headers, data):
        res = requests.post(url=url,json=headers,data=data).json()
        return res

    def run_main(self, url, method, headers, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, headers, data)
        else:
            res = self.send_post(url, headers, data)
        return res

if __name__ == "__main__":
    test = RunMain();
    url = 'http://gzapi.tnaot.com:818/api/home/open_app?appid=2017002&appkey=62345451mj56f454&channelId=Tnaot&clientName=5.2.0'
    headers = {'Host': 'gzapi.tnaot.com:818', 'device_mac': '54:B1:21:9F:03:50', 'app_version': '5.2.0', 'debug': 0, 'device_id': 'F9D32D7B74010783BE2B70D053844F7D08B0A750', 'device_model': 'vivo X9i', 'device_type': 1, 'lan': 'en-US'}
    data = []
    # test.run_main(url,method='GET',headers=headers, data=data)
    print(test.run_main(url,method='GET',headers=headers, data=data))

    # r = requests.get(url='http://gzapi.tnaot.com:818/api/home/open_app?appid=2017002&appkey=62345451mj56f454&channelId=Tnaot&clientName=5.2.0',
    #                  params={'Host': 'gzapi.tnaot.com:818', 'device_mac': '54:B1:21:9F:03:50', 'app_version': '5.2.0', 'debug': 0, 'device_id': 'F9D32D7B74010783BE2B70D053844F7D08B0A750', 'device_model': 'vivo X9i', 'device_type': 1, 'lan': 'en-US'})
    #
    #
    # print(r.json())
    # print()

# class TestMethod(unittest.TestCase):
#     def setUp(self):
#         self.run = RunMain()
#
#     def test_01(self):
#         url = 'http://api.ishugui.com/asg/portal/call/265.do'
#         data = {
#             "sstoken": "eyJleHAiOjE1Njg1MzgyNTczMzUsImlhdCI6MTU2MDc2MjI1NzMzNSwicHAiOiIxMTQwNTQ1Njg5MDYwMDQ0ODAwQHNvaHUuY29tIiwidGsiOiIwZkNYSHpjTUZzR0dFMEswbVdvUVFCNWVCanpXa0hmWiIsInYiOjB9.SDYkT9FpWrBbko6xRrESN74IXJhzkqQLtijKjGiVrqA",
#             "gidinf": "x011060802ff0fd40695d68140002799751474c540b3",
#             "ppinf": "2|1560762257|1561971857|bG9naW5pZDowOnx1c2VyaWQ6Mjg6MTE0MDU0NTY4OTA2MDA0NDgwMEBzb2h1LmNvbXxzZXJ2aWNldXNlOjMwOjAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMHxjcnQ6MTA6MjAxOS0wNi0xN3xlbXQ6MTowfGFwcGlkOjY6MTEwNjA4fHRydXN0OjE6MXxwYXJ0bmVyaWQ6MTowfHJlbGF0aW9uOjA6fHV1aWQ6MTY6czk1YWIwNDk5NjE3YmJhNnx1aWQ6MTY6czk1YWIwNDk5NjE3YmJhNnx1bmlxbmFtZTowOnw",
#             "pprdig": "kaKPdU0WwIdzL58CqxNz5pgMyv23P0-Y5GRnd5ufPlXIGzrk7_7TlIK5XFQiuoqAHNqGVXHCVd4cB1DIkR5yFZ_nExnSjIZbBJWYlMkrsiIjDYqWCvedZRLm8sZqS0WqA0FcKXuSn3Z0gVRus9YpEonNz5wyuWdUqxaSmzlzygY",
#             "ppsmu": "1|1560762257|1561971857|dXNlcmlkOjI4OjExNDA1NDU2ODkwNjAwNDQ4MDBAc29odS5jb218dWlkOjA6fHV1aWQ6MDo|byWcaoPqy02s2_9GHLhZFAQ6Ov_GazMPFLrq115HiSTBS9Ijr33a55quRq2Mr1_6ZMruKEk-BYFpShUaMtwRYA"
#         }
#         res1 = self.run.run_main(url, "POST", json.dumps(data))
#         print(res1)
#
#     def test_02(self):
#         url = 'http://api.ishugui.com/asg/portal/call/265.do'
#         data = {
#
#         }
#         res2 = self.run.run_main(url, 'POST', data)
#
#         print(res2)
#
#
# if __name__ == '__main__':
#     unittest.main()