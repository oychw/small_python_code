#!/usr/bin/env python
# coding=utf-8
"""
Demo methods of unittest!
Copyright 2015.04.25 Rongzhong.Xu
http://automationtesting.sinaapp.com
"""


import unittest


class TestDemo(unittest.TestCase):

    """
    Demo methods of unittest!
    """

    def test_assert_equal(self):
        self.assertEqual(1, 1)

    def test_assert_almost_equal_delta_0_5(self):
        self.assertAlmostEqual(1, 1.2, delta=0.5)

    def test_assert_almost_equal_places(self):
        self.assertAlmostEqual(1, 1.00001, places=4)

    def test_assert_raises(self):
        self.assertRaises(ValueError, int, "a")

    def test_assert_raises_alternative(self):
        with self.assertRaises(AttributeError):
            [].get

    def test_assert_dict_contains_subset(self):
        expected = {'a': 'b'}
        actual = {'a': 'b', 'c': 'd', 'e': 'f'}
        self.assertDictContainsSubset(expected, actual)

    def test_assert_dict_equal(self):
        expected = {'a': 'b', 'c': 'd'}
        actual = {'c': 'd', 'a': 'b'}
        self.assertDictEqual(expected, actual)

    def test_assert_true(self):
        self.assertTrue(1)
        self.assertTrue("Hello, World")

    def test_assert_false(self):
        self.assertFalse(0)
        self.assertFalse("")

    def test_assert_greater(self):
        self.assertGreater(2, 1)

    def test_assert_greater_equal(self):
        self.assertGreaterEqual(2, 2)

    def test_assert_in(self):
        self.assertIn(1, [1, 2, 3, 4, 5])

    def test_assert_is(self):
        self.assertIs("a", "a")

    def test_assert_is_instance(self):
        self.assertIsInstance(1, int)

    def test_assert_is_not_instance(self):
        self.assertNotIsInstance(1, str)

    def test_assert_is_none(self):
        self.assertIsNone(None)

    def test_assert_is_not(self):
        self.assertIsNot([], [])

    def test_assert_is_not_none(self):
        self.assertIsNotNone(1)

    def test_assert_less(self):
        self.assertLess(1, 2)

    def test_assert_less_equal(self):
        self.assertLessEqual(2, 2)

    def test_assert_items_equal(self):
        self.assertItemsEqual([1, 2, 3], [3, 1, 2])

if __name__ == '__main__':
    unittest.main()
