# -*- coding: utf-8 -*-
# @Time : 2020/1/23 14:56
# @Author : jwh5566
# @Email : jwh5566@aliyun.com
# @File : capture_output.py

import subprocess

res = subprocess.run('ls', '-l', stdout=subprocess.PIPE)
print('returncode:', res.returncode)
print('{} bytes in stdout:\n{}'.format(len(res.stdout), res.stdout.decode('utf-8')))
