#!/usr/bin/env python3
# coding: utf-8

"""sci

####
矩阵
####

矩阵（`Matrix <http://mathworld.wolfram.com/Matrix.html>`_）
  一个 :math:`m \\times n` 矩阵是一个由 :math:`m` 行 :math:`n` 列元素排列成的矩形阵列。

"""

__author__ = 'zhengrr'

import numpy as np
import pandas as pd
import unittest


class TestClass(unittest.TestCase):
    def test_matrix_3_5(self):
        """一个三行五列数字矩阵 :math:`\\mathbf{A}`

        .. math::

          \\mathbf{A} = \\begin{bmatrix}
            1  & 2  & 3  & 4  & 5 \\\\
            6  & 7  & 8  & 9  & 10 \\\\
            11 & 12 & 13 & 14 & 15
          \\end{bmatrix}
        """
        pass


if __name__ == '__main__':
    unittest.main()
