# -*- coding: utf-8 -*-
# @Time : 2020/1/23 13:59
# @Author : jwh5566
# @Email : jwh5566@aliyun.com
# @File : redirection.py

import sys


class Redirection(object):
    def __init__(self, in_obj, out_obj):
        self.input = in_obj
        self.output = out_obj

    def read_line(self):
        res = self.input.readline()
        self.output.write(res)
        return res


if __name__ == '__main__':
    if not sys.stdin.isatty():
        sys.stdin = Redirection(in_obj=sys.stdin, out_obj=sys.stdout)
    a = input("输入一个字符串: ")
    b = input("输入另外一个字符串: ")
    print("输入的字符串是: ", repr(a), "and", repr(b))
