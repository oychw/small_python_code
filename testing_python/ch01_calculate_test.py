#!/usr/bin/env python
# coding=utf-8
"""
Demo simple unittest!
Copyright 2015.04.17 Rongzhong.Xu
http://automationtesting.sinaapp.com
"""


import unittest
from ch01_calculate import Calculate


class TestCalculate(unittest.TestCase):
    """
    Calculator unittest
    """
    def setUp(self):
        self.calc = Calculate()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))


if __name__ == '__main__':
    unittest.main()
