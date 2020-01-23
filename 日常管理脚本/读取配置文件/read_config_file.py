# -*- coding: utf-8 -*-
# @Time : 2020/1/23 15:24
# @Author : jwh5566
# @Email : jwh5566@aliyun.com
# @File : read_config_file.py

from configparser import ConfigParser

p = ConfigParser()
p.read('read_simple.ini')
print(p.get('bug_tracker', 'url'))

