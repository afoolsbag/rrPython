#!/usr/bin/env python3
# coding: utf-8

"""
- `前提条件和准备工作 <https://developers.google.com/machine-learning/crash-course/prereqs-and-prework>`_

- `创建和操控张量 <https://colab.research.google.com/notebooks/mlcc/creating_and_manipulating_tensors.ipynb>`_
"""

import tensorflow as tf
import unittest as ut

try:
    tf.contrib.eager.enable_eager_execution()
except ValueError:
    pass


class TestCase(ut.TestCase):

    def test_vector_addition(self):
        """
        矢量加法
        """
        primes = tf.constant([2, 3, 5, 7, 11, 13], dtype=tf.int32)
        print('primes:')
        print(primes)
        print()

        ones = tf.ones([6], dtype=tf.int32)
        print('ones:')
        print(ones)
        print()

        just_beyond_primes = tf.add(primes, ones)
        print('just_beyond_primes:')
        print(just_beyond_primes)
        print()

        twos = tf.constant([2, 2, 2, 2, 2, 2], dtype=tf.int32)
        print('tows:')
        print(twos)
        print()

        primes_doubled = primes * twos
        print('primes_doubled:')
        print(primes_doubled)
        print()

        some_matrix = tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.int32)
        print('some_matrix:')
        print(some_matrix)
        print()

        print('value of some_matrix is:')
        print(some_matrix.numpy())
        print()

    def test_shape(self):
        """张量形状"""
        # 标量（0 维张量）
        scalar = tf.constant('0')

        # 矢量（1 维张量）
        vector = tf.constant(['1', '2', '3'])

        # 矩阵（2 维张量）
        matrix = tf.constant([['1-1', '1-2', '1-3', '1-4'],
                              ['2-1', '2-2', '2-3', '2-4'],
                              ['3-1', '3-2', '3-3', '3-4']])

        print('scalar has shape', scalar.get_shape(), 'and value:\n', scalar.numpy())
        print('vector has shape', vector.get_shape(), 'and value:\n', vector.numpy())
        print('matrix has shape', matrix.get_shape(), 'and value:\n', matrix.numpy())

    def test_broadcasting(self):
        """张量广播"""
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

        ::

            t8x2    t2x8
            1  2    1  2  3  4  5  6  7  8
            3  4    9  10 11 12 13 14 15 16
            5  6
            7  8    t4x4
            9  10   1  2  3  4
            11 12   5  6  7  8
            13 14   9  10 11 12
            15 16   13 14 15 16

        ::

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
