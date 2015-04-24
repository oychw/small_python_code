#!/usr/bin/env python
# coding=utf-8
"""
Demo simple test!
Copyright 2015.04.24 Rongzhong.Xu
http://automationtesting.sinaapp.com
"""


class Calculate(object):
    """
    Calculator
    """
    @classmethod
    def add(cls, num1, num2):
        """Add"""
        if isinstance(num1, int) and isinstance(num1, int):
            return num1 + num2
        else:
            raise TypeError("Invalid type: {} and {}".format(type(num1),
                                                             type(num2)))

if __name__ == '__main__':
    CALC = Calculate()
    RESULT = CALC.add(2, 2)
    print(RESULT)
