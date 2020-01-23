# -*- coding: utf-8 -*-
# @Time : 2020/1/23 15:08
# @Author : jwh5566
# @Email : jwh5566@aliyun.com
# @File : with_prompt.py

import getpass

try:
    p = getpass.getpass("输入密码: ")
except Exception as error:
    print('ERROR', error)
else:
    print('密码是', p)
