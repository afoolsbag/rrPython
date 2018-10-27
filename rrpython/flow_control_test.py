#!/usr/bin/env python3
# coding: utf-8

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
            pass

    def test_while(self):
        while random.randint(0, 1):
            pass


if __name__ == '__main__':
    unittest.main()
