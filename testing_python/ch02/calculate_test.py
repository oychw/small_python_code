#!/usr/bin/env python
# coding=utf-8
"""
Demo simple unittest!
Copyright 2015.04.27 Rongzhong.Xu
xurongzhong#126.com
http://automationtesting.sinaapp.com
"""


import unittest
from calculate import Calculate


class TestCalculate(unittest.TestCase):

    """
    Calculator unittest
    """

    def setUp(self):
        self.calc = Calculate()

    def test_add_method_returns_correct_result(self):
        print('\nHello, We can show information on screen!\n')
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertAlmostEquals(1, 1)


if __name__ == '__main__':
    unittest.main()
