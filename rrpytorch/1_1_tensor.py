#!/usr/bin/env python3
# coding: utf-8

"""张量（tensor）"""

__author__ = 'zhengrr'

import torch
import unittest


class TestTensor(unittest.TestCase):

    def test_empty_tensor(self):
        """全零张量"""
        x = torch.empty(5, 3)
        print(x)

    def test_random_tensor(self):
        """随机张量"""
        x = torch.rand(5, 3)
        print(x)

    def test_zeros_tensor(self):
        """全零张量"""
        x = torch.zeros(5, 3, dtype=torch.long)
        print(x)

    def test_initial_tensor(self):
        """给定初值的张量"""
        x = torch.tensor([1, 2, 3, 4, 5])
        print(x)

    def test_ones_tensor(self):
        """全一张量"""
        x = torch.ones(5, 3, dtype=torch.double)
        print(x)

    def test_tensor_size(self):
        """张量尺寸"""
        x = torch.rand(5, 3)
        print(x.size())

    def test_tensor_add(self):
        """张量加法"""
        x = torch.ones(5, 3)
        y = torch.ones(5, 3)

        z1 = x + y
        z2 = torch.add(x, y)
        z3 = torch.empty(5, 3)
        torch.add(x, y, out=z3)
        x.add_(y)

        self.assertTrue(torch.equal(z1, z2))
        self.assertTrue(torch.equal(z2, z3))
        self.assertTrue(torch.equal(z3, x))

    def test_tensor_view(self):
        """改变张量维度"""
        x = torch.rand(4, 4)
        print(x)
        print(x.view(-1, 8))


if __name__ == '__main__':
    unittest.main()
