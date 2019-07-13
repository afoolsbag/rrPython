#!/usr/bin/env python3
# coding: utf-8

__author__ = 'zhengrr'

import unittest
import random


class TestFlowControl(unittest.TestCase):

    def test_if(self):
        if random.randint(0, 1):
            pass
        elif random.randint(0, 1):
            pass
        else:
            pass

    def test_for_in(self):
        for x in range(10):
            print('x:', x)

    TD = {'kSMT': 'vSMT', 'kZL': 'vZl', 'kJT': 'vJT'}

    def test_for_in_dict_key(self):
        for key in self.TD:
            print('key:', key)

    def test_for_in_dict_value(self):
        for value in self.TD.values():
            print('value:', value)

    def test_for_in_dict_pair(self):
        for key, value in self.TD.items():
            print('key:', key, 'value:', value)

    def test_for_in_dict_index(self):
        for index, value in enumerate(self.TD):
            print('index:', index, 'value:', value)

    def test_while(self):
        while random.randint(0, 1):
            pass


if __name__ == '__main__':
    unittest.main()
