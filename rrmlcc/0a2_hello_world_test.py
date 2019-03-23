#!/usr/bin/env python3
# coding: utf-8

"""
**学习目标**：

- 运行 TensorFlow 程序
"""

import tensorflow as tf
import unittest as ut

try:
    tf.contrib.eager.enable_eager_execution()
except ValueError:
    pass


class TestHelloWorld(ut.TestCase):

    def test_hello_world(self):
        """
        输出 pandas API 版本。
        """

        tf_const = tf.constant('Hello, world!')
        tf_value = tf_const.numpy()
        print(tf_value)


if __name__ == '__main__':
    ut.main()
