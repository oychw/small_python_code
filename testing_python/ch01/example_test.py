#!/usr/bin/env python
# coding=utf-8
"""
Demo simple unittest!
Copyright 2015.04.25 Rongzhong.Xu
http://automationtesting.sinaapp.com
"""


import unittest


class TestDemo(unittest.TestCase):
    """
    assertRaises demo
    """
    def test_assert_raises(self):
        """assertRaises demo"""
        self.assertRaises(AttributeError, [].get)

if __name__ == '__main__':
    unittest.main()
