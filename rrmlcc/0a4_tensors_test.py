#!/usr/bin/env python3
# coding: utf-8

"""
**学习目标**：

- 初始化 TensorFlow ``Variable`` 并赋值
- 创建和操控张量
- 回忆线性代数中的加法和乘法知识（参阅矩阵
  `加法 <https://wikipedia.org/wiki/Matrix_addition>`_ 和
  `乘法 <https://wikipedia.org/wiki/Matrix_multiplication>`_ 简介）
- 熟悉基本的 TensorFlow 数学和数组运算
"""

import tensorflow as tf
import unittest as ut

try:
    tf.contrib.eager.enable_eager_execution()
except ValueError:
    pass


class TestTensors(ut.TestCase):

    def test_vector_addition(self):
        """
        矢量加法

        您可以对张量执行很多典型数学运算 (`TF API <https://tensorflow.org/api_guides/python/math_ops>`_)。
        以下代码会创建下列矢量（一维张量），所有矢量都正好有六个元素：

        - 一个包含质数的 ``primes`` 矢量。
        - 一个值全为 ``1`` 的 ``ones`` 矢量。
        - 一个通过对前两个矢量执行元素级加法而创建的矢量。
        - 一个通过将 ``primes`` 矢量中的元素翻倍而创建的矢量。
        """
        primes = tf.constant([2, 3, 5, 7, 11, 13], dtype=tf.int32)
        print('primes:', primes)

        ones = tf.ones([6], dtype=tf.int32)
        print('ones:', ones)

        just_beyond_primes = tf.add(primes, ones)
        print('just_beyond_primes:', just_beyond_primes)

        twos = tf.constant([2, 2, 2, 2, 2, 2], dtype=tf.int32)
        print('tows:', twos)

        primes_doubled = primes * twos
        print('primes_doubled:', primes_doubled)

    def test_numpy(self):
        """
        输出张量不仅会返回其值，还会返回其形状（将在下一部分中讨论）以及存储在张量中的值的类型。
        调用张量的 ``numpy`` 方法会返回该张量的值（以 NumPy 数组形式）
        """
        some_matrix = tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.int32)

        print('some_matrix is:\n', some_matrix)
        print('value of some_matrix is:\n', some_matrix.numpy())

    def test_shape(self):
        """
        张量形状

        形状用于描述张量维度的大小和数量。
        张量的形状表示为 ``list``，其中第 ``i`` 个元素表示维度 ``i`` 的大小。
        列表的长度表示张量的阶（即维数）。

        有关详情，请参阅 `TensorFlow 文档 <https://tensorflow.org/programmers_guide/tensors#shape>`_。

        以下是一些基本示例：
        """
        # A scalar (0-D tensor).
        scalar = tf.zeros([])

        # A vector with 3 elements.
        vector = tf.zeros([3])

        # A matrix with 2 rows and 3 columns.
        matrix = tf.zeros([2, 3])

        print('scalar has shape', scalar.get_shape(), 'and value:\n', scalar.numpy())
        print('vector has shape', vector.get_shape(), 'and value:\n', vector.numpy())
        print('matrix has shape', matrix.get_shape(), 'and value:\n', matrix.numpy())

    def test_broadcasting(self):
        """
        广播

        在数学中，您只能对形状相同的张量执行元素级运算（例如，*相加* 和 *等于*）。
        不过，在 TensorFlow 中，您可以对张量执行传统意义上不可行的运算。
        TensorFlow 支持 **广播** （一种借鉴自 NumPy 的概念）。
        利用广播，元素级运算中的较小数组会增大到与较大数组具有相同的形状。
        例如，通过广播：\n",

        - 如果运算需要大小为 ``[6]`` 的张量，则大小为 ``[1]`` 或 ``[]`` 的张量可以作为运算数。
        - 如果运算需要大小为 ``[4, 6]`` 的张量，则以下任何大小的张量都可以作为运算数：

          - ``[1, 6]``
          - ``[6]``
          - ``[]``

        - 如果运算需要大小为 ``[3, 5, 6]`` 的张量，则以下任何大小的张量都可以作为运算数：

          - ``[1, 5, 6]``
          - ``[3, 1, 6]``
          - ``[3, 5, 1]``
          - ``[1, 1, 1]``
          - ``[5, 6]``
          - ``[1, 6]``
          - ``[6]``
          - ``[1]``
          - ``[]``

        注意：当张量被广播时，从概念上来说，系统会 **复制** 其条目
        （出于性能考虑，实际并不复制。广播专为实现性能优化而设计）。

        有关完整的广播规则集，请参阅简单易懂的 `NumPy 广播文档 <http://docs.scipy.org/doc/numpy-1.10.1/user/basics.broadcasting.html>`_

        以下代码执行了与之前一样的张量运算，不过使用的是标量值（而不是全包含 ``1`` 或全包含 ``2`` 的矢量）和广播。"
        """
        primes = tf.constant([2, 3, 5, 7, 11, 13], dtype=tf.int32)
        print('primes: ', primes)

        one = tf.constant(1, dtype=tf.int32)
        print('one:', one)

        just_beyond_primes = tf.add(primes, one)
        print('just_beyond_primes:', just_beyond_primes)

        two = tf.constant(2, dtype=tf.int32)
        primes_doubled = primes * two
        print('primes_doubled:', primes_doubled)

    def test_matrix_multiplication(self):
        """
        矩阵乘法

        在线性代数中，当两个矩阵相乘时，第一个矩阵的 *列* 数必须等于第二个矩阵的 *行* 数。

        - ``3x4`` 矩阵乘以 ``4x2`` 矩阵是 **有效** 的，可以得出一个 ``3x2`` 矩阵。
        - ``4x2`` 矩阵乘以 ``3x4`` 矩阵是 **无效** 的。

        m x n 矩阵（m 行 n 列矩阵）::

                |--------- n ---------|
            - [1,1] [1,2] [1,3] ... [1,n]
            | [2,1] [2,2] [2,3] ... [2,n]
            m [3,1] [3,2] [3,3] ... [3,n]
            | ...   ...   ...   ... ...
            - [m,1] [m,2] [m,3] ... [m,n]

        矩阵相乘::

               x--------------------------B[1,1] B[1,2]
               |   +  x-------------------B[2,1] B[2,2]
               |      |   +  x------------B[3,1] B[3,2]
               |      |      |   +  x-----B[4,1] B[4,2]
               |      |      |      |   =
            A[1,1] A[1,2] A[1,3] A[1,4]   C[1,1] ...
            A[2,1] A[2,2] A[2,3] A[2,4]   ...    ...
            A[3,1] A[3,2] A[3,3] A[3,4]   ...    ...
        """
        # A 3x4 matrix (2-d tensor).
        m_3_4 = tf.constant([[5, 2, 4, 3], [5, 1, 6, -2], [-1, 3, -1, -2]],
                            dtype=tf.int32)

        # A 4x2 matrix (2-d tensor).
        m_4_2 = tf.constant([[2, 2], [3, 5], [4, 5], [1, 6]], dtype=tf.int32)

        # Multiply `m_3_4` by `m_4_2`; result is 3x2 matrix.
        matrix_multiply_result = tf.matmul(m_3_4, m_4_2)

        print(matrix_multiply_result)

    def test_reshape(self):
        """
        张量变形

        由于张量加法和矩阵乘法均对运算数施加了限制条件，TensorFlow 编程者需要频繁改变张量的形状。

        您可以使用 ``tf.reshape`` 方法改变张量的形状。
        例如，您可以将 8x2 张量变形为 2x8 张量或 4x4 张量::

            t8x2    t2x8
            1  2    1  2  3  4  5  6  7  8
            3  4    9  10 11 12 13 14 15 16
            5  6
            7  8    t4x4
            9  10   1  2  3  4
            11 12   5  6  7  8
            13 14   9  10 11 12
            15 16   13 14 15 16

        此外，您还可以使用 ``tf.reshape`` 更改张量的维数（“阶”）。
        例如，您可以将 8x2 张量变形为三维 2x2x4 张量或一维 16 元素张量::

            t8x2    t2x2x4
            1  2    1  2  3  4
            3  4    5  6  7  8
            5  6      9  10 11 12
            7  8      13 14 15 16
            9  10
            11 12
            13 14   t16
            15 16   1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
        """
        # Create an 8x2 matrix (2-D tensor).
        matrix = tf.constant(
            [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]],
            dtype=tf.int32)

        reshaped_2x8_matrix = tf.reshape(matrix, [2, 8])
        reshaped_4x4_matrix = tf.reshape(matrix, [4, 4])

        reshaped_2x2x4_tensor = tf.reshape(matrix, [2, 2, 4])
        one_dimensional_vector = tf.reshape(matrix, [16])

        print("Original matrix (8x2):")
        print(matrix.numpy())

        print("Reshaped matrix (2x8):")
        print(reshaped_2x8_matrix.numpy())
        print("Reshaped matrix (4x4):")
        print(reshaped_4x4_matrix.numpy())

        print("Reshaped 3-D tensor (2x2x4):")
        print(reshaped_2x2x4_tensor.numpy())
        print("1-D vector:")
        print(one_dimensional_vector.numpy())


if __name__ == '__main__':
    ut.main()
