#!/usr/bin/env python3
# coding: utf-8

"""
- `前提条件和准备工作 <https://developers.google.com/machine-learning/crash-course/prereqs-and-prework>`_

- `TensorFlow 编程概念 <https://colab.research.google.com/notebooks/mlcc/tensorflow_programming_concepts.ipynb>`_
"""

import tensorflow as tf

# 图
g = tf.Graph()
with g.as_default():
    # 指令 Operation
    op_x = tf.constant(8, name='x_const')
    op_y = tf.constant(5, name='y_const')
    op_sum_xy = tf.add(op_x, op_y, name='x_y_sum')

    op_z = tf.constant(4, name='z_const')
    op_sum_xyz = tf.add(op_sum_xy, op_z, name='x_y_z_sum')

    with tf.Session() as s:
        print(op_sum_xyz.eval())
