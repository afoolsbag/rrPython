#!/usr/bin/env python3
# coding: utf-8

import unittest


def power(base: float, exponent=2):
    p = 1.
    for x in range(exponent):
        p *= base
    return p


def average(*nums):
    return sum(nums) / len(nums)


def makedict(*, k1, k2, **kw) -> dict:
    kw['k1'] = k1
    kw['k2'] = k2
    return kw


class TestFunction(unittest.TestCase):

    def test_power(self):
        self.assertEqual(power(3), 9)

    def test_average(self):
        self.assertEqual(average(5, 7), 6)


if __name__ == '__main__':
    unittest.main()
