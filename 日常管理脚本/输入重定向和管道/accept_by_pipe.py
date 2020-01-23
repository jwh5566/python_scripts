# -*- coding: utf-8 -*-
# @Time : 2020/1/23 14:10
# @Author : jwh5566
# @Email : jwh5566@aliyun.com
# @File : accept_by_pipe.py

import sys

for n in sys.stdin:
    print(int(n.strip()) // 2)
