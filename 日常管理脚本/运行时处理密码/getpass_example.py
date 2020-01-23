# -*- coding: utf-8 -*-
# @Time : 2020/1/23 15:11
# @Author : jwh5566
# @Email : jwh5566@aliyun.com
# @File : getpass_example.py

import getpass

passwd = getpass.getpass("输入密码: ")
if passwd.lower() == 'jwh6867285':
    print('welcome!')
else:
    print('密码不对!')
