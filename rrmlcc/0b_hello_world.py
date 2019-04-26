#!/usr/bin/env python3
# coding: utf-8

"""
- `前提条件和准备工作 <https://developers.google.com/machine-learning/crash-course/prereqs-and-prework>`_

- `准备工作：Hello World <https://colab.research.google.com/notebooks/mlcc/hello_world.ipynb>`_
"""

import tensorflow as tf

try:
    tf.contrib.eager.enable_eager_execution()
except ValueError:
    pass

tf_const = tf.constant('Hello, world!')
tf_value = tf_const.numpy()
print(tf_value)
