# -*- coding: utf-8 -*-
# @Time : 2020/1/23 15:13
# @Author : jwh5566
# @Email : jwh5566@aliyun.com
# @File : password_prompt_again.py

import getpass

user_name = getpass.getuser()
print("用户名: %s" % user_name)
while True:
    passwd = getpass.getpass("输入密码: ")
    if passwd == "jwh6867285":
        print("Welcome!")
        break
    else:
        print("密码不对!")
