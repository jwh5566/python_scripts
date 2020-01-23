# -*- coding: utf-8 -*-
# @Time : 2020/1/23 13:40
# @Author : jwh5566
# @Email : jwh5566@aliyun.com
# @File : test_if.py

import unittest

import if_example


class Test_if(unittest.TestCase):
    def test_if(self):
        result = if_example.check_if()
        self.assertEqual(result, 100)


if __name__ == '__main__':
    unittest.main()
