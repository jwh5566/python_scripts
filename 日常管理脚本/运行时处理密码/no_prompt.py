# -*- coding: utf-8 -*-
# @Time : 2020/1/23 15:05
# @Author : jwh5566
# @Email : jwh5566@aliyun.com
# @File : no_prompt.py

import getpass

try:
    p = getpass.getpass()
except Exception as error:
    print("ERROR", error)
else:
    print('Password enterd:', p)
