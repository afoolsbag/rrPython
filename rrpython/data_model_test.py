#!/usr/bin/env python3
# coding: utf-8

import unittest


class TestDataModel(unittest.TestCase):

    def test_none(self):
        n = None
        self.assertIs(n, None)

    def test_not_implemented(self):
        n = NotImplemented
        self.assertIs(n, NotImplemented)

    def test_ellipsis(self):
        e = ...
        self.assertIs(e, Ellipsis)

    def test_numbers(self):
        i = 0
        self.assertIs(type(i), int)

        b = False
        self.assertIs(type(b), bool)

        r = 0.0
        self.assertIs(type(r), float)

        c = 0j
        self.assertIs(type(c), complex)

    def test_sequences(self):
        s = ''
        self.assertIs(type(s), str)

        t = ()
        self.assertIs(type(t), tuple)

        b = b''
        self.assertIs(type(b), bytes)

        ls = []
        self.assertIs(type(ls), list)

        ba = bytearray(b'')
        self.assertIs(type(ba), bytearray)

    def test_sets(self):
        s = {0}
        self.assertIs(type(s), set)

        fs = frozenset({0})
        self.assertIs(type(fs), frozenset)

    def test_mappings(self):
        d = {}
        self.assertIs(type(d), dict)


if __name__ == '__main__':
    unittest.main()
