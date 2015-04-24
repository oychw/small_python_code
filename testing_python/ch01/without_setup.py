#!/usr/bin/env python
# coding=utf-8
"""
Demo simple unittest!
Copyright 2015.04.17 Rongzhong.Xu
http://automationtesting.sinaapp.com
"""


import unittest
from ch01_calculate_int import Calculate


class TestCalculate(unittest.TestCase):

    """
    Calculator unittest
    """

    def test_add_method_returns_correct_result(self):
        calc = Calculate()
        self.assertEqual(4, calc.add(2, 2))

    def test_add_method_raises_typeerror_if_not_ints(self):
        calc = Calculate()
        self.assertRaises(TypeError, calc.add, "Hello", "World")

if __name__ == '__main__':
    unittest.main()
