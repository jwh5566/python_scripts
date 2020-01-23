# -*- coding: utf-8 -*-
# @Time : 2020/1/23 15:26
# @Author : jwh5566
# @Email : jwh5566@aliyun.com
# @File : read_many_config_file.py

from configparser import ConfigParser

p = ConfigParser()
files = ['hello.ini', 'bye.ini', 'read_simple.ini', 'welcome.ini']
files_found = p.read(files)

files_missing = set(files) - set(files_found)

print('找到文件:', sorted(files_found))
print('丢失文件:', sorted(files_missing))

