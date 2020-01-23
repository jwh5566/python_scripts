# -*- coding: utf-8 -*-
# @Time : 2020/1/23 11:13
# @Author : jwh5566
# @Email : jwh5566@aliyun.com
# @File : pdb_example.py
import pdb


class Student:
    def __init__(self, std):
        self.count = std

    def print_sed(self):
        for i in range(self.count):
            pdb.set_trace()
            print(i)
        return


if __name__ == '__main__':
    Student(5).print_sed()
