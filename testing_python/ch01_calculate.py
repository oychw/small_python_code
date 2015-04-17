#!/usr/bin/env python
# coding=utf-8
"""
Demo simple test!
"""


class Calculate(object):
    """
    Calculator
    """
    @classmethod
    def add(cls, num1, num2):
        """Add"""
        return num1 + num2


if __name__ == '__main__':
    CALC = Calculate()
    RESULT = CALC.add(2, 2)
    print RESULT
