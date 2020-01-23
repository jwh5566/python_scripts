# -*- coding: utf-8 -*-
# @Time : 2020/1/23 10:10
# @Author : jwh5566
# @Email : jwh5566@aliyun.com
# @File : test1.py

# import sys
# print('参数个数: ', len(sys.argv))
# print('参数列表: ', str(sys.argv))
# a = 10
# if a > 0:
#     print(a, "是一个正数")
# print("总是打印这句话")
#
# a = -10
# if a > 0:
#     print(a, "是一个正数")

# a = 10
# if a > 50:
#     print("a is greater than 50")
# elif a == 10:
#     print("a is equal to 10")
# else:
#     print("a is negative")

# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# sum = 0
# for i in numbers:
#     sum += i
#     print("The sum is: ", sum)

# for i in range(5):
#     print("The number is", i)

# a = 10
# sum = 0
# i = 1
# while i <= a:
#     sum += i
#     i += 1
#     print("The sum is", sum)

# numbers = [10, 25, 54, 86, 89, 11, 33, 22]
# new_numbers = filter(lambda x: (x%2 == 0), numbers)
# print(type(new_numbers))
# print(list(new_numbers))

# my_List = [1, 5, 4, 6, 8, 11, 3, 12]
# new_list = list(map(lambda x: x*2, my_List))
# print(new_list)

a = 35
b = 57
try:
    c = a + b
    print("the value of c is: ", c)
    d = b / 0
    print("the value d is ", d)
except:
    print("division by zero is not possible")
print("out if try ... except block")
