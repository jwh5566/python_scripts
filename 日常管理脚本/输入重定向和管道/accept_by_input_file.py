# -*- coding: utf-8 -*-
# @Time : 2020/1/23 14:16
# @Author : jwh5566
# @Email : jwh5566@aliyun.com
# @File : accept_by_input_file.py

i = open('sample.txt', 'r')
o = open('sample_output.txt', 'w')
a = i.read()
o.write(a)
