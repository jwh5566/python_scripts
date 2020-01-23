# -*- coding: utf-8 -*-
# @Time : 2020/1/23 11:26
# @Author : jwh5566
# @Email : jwh5566@aliyun.com
# @File : cprof_example.py

mul_value = 0


def mul_numbers(num1, num2):
    mul_value = num1 * num2
    print("local value: ", mul_value)
    return mul_value


mul_numbers(58, 77)
print("global value: ", mul_value)
