# -*- coding: utf-8 -*-
# @Time : 2020/1/23 11:40
# @Author : jwh5566
# @Email : jwh5566@aliyun.com
# @File : test_addition.py

import unittest

import arithmetic


class Test_addition(unittest.TestCase):
    # Test Integers
    def test_add_numbers_int(self):
        sum = arithmetic.add_numbers(50, 50)
        self.assertEqual(sum, 100)

    # Test Floats
    def test_add_numbers_float(self):
        sum = arithmetic.add_numbers(50.55, 78)
        self.assertEqual(sum, 128.55)

    # Test Strings
    def test_add_numbers_strings(self):
        sum = arithmetic.add_numbers('hello', 'python')
        self.assertEqual(sum, 'hellopython')


if __name__ == '__main__':
    unittest.main()
