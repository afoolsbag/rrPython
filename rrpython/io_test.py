#!/usr/bin/env python3
# coding: utf-8

__author__ = 'zhengrr'

from os import remove
from time import sleep
import unittest


class TestIO(unittest.TestCase):

    def test_write_file(self):
        f = None
        try:
            f = open('test.txt', 'w')
            f.write('hello, world')
        finally:
            if f:
                f.close()

    def test_read_file(self):
        sleep(1)
        with open('test.txt', 'r') as f:
            print(f.read(1024))
        sleep(1)
        remove('test.txt')


if __name__ == '__main__':
    unittest.main()
