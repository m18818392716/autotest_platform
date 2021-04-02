#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/20 18:30
# @Author  : Susanna
# @Email   : m18818392716@163.com
# @File    : config.py
# @Software: PyCharm

import os
field_excel = ['编号',
               '接口名称',
               '用例级别',
               '请求类型',
               '接口地址',
               '接口头文件',
               '接口请求参数',
               '接口返回包',
               '待比较参数',
               '实际参数值',
               '预期参数值',
               '参数值比较结果',
               '待比较参数集合',
               '实际参数集合',
               '参数完整性结果',
               '用例状态',
               '创建时间',
               '更新时间',
               ] # 到处Excel的表格标题
src_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) #当前代码所在目录的上级目录
#测试环境数据库配置，默认测试环境
host_test='127.0.0.1'
user_test='root'
password_test='123456'
name_test='test_interface'
port_test=3306
#生产环境数据库配置