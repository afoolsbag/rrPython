#!/usr/bin/env python3
# coding: utf-8

"""
**学习目标**：

- 运行 TensorFlow 程序
"""

import tensorflow as tf

try:
    tf.contrib.eager.enable_eager_execution()
except ValueError:
    pass

tf_const = tf.constant('Hello, world!')
tf_value = tf_const.numpy()
print(tf_value)
