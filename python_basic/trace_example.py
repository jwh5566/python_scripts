# -*- coding: utf-8 -*-
# @Time : 2020/1/23 11:22
# @Author : jwh5566
# @Email : jwh5566@aliyun.com
# @File : trace_example.py

class Student:
    def __init__(self, std):
        self.count = std

    def go(self):
        for i in range(self.count):
            print(i)


if __name__ == '__main__':
    Student(5).go()
