#!/usr/bin/env python3
# coding: utf-8

"""sci

####
映射 （`Map <http://mathworld.wolfram.com/Map.html>`_）
####

设集合 :math:`X` 和集合 :math:`Y` 是两个非空集合，
对于集合 :math:`X` 中任一元素 :math:`x`，依照某种规律 :math:`f`，恒有集合 :math:`Y` 中唯一确定元素 :math:`y` 与之对应，
则称对应规律 :math:`f` 为一个从集合 :math:`X` 到集合 :math:`Y` 的映射，
记作 :math:`f: X \\to Y` 或 :math:`f: x \\mapsto y`。
其中

* 集合 :math:`X` 称为映射 :math:`f` 的定义域（`Domain <http://mathworld.wolfram.com/Domain.html>`_）
* 集合 :math:`Y` 称为映射 :math:`f` 的陪域（`Codomain <http://mathworld.wolfram.com/Codomain.html>`_）
* 元素 :math:`x` 称为在映射 :math:`f` 下，元素 :math:`y` 的原像（`Preimage <http://mathworld.wolfram.com/Preimage.html>`_）
* 元素 :math:`y` 称为在映射 :math:`f` 下，元素 :math:`x` 的像（`Image <http://mathworld.wolfram.com/Image.html>`_），记作 :math:`y = f(x)`
* 集合 :math:`R_f = \\{ f(x) | x \\in X \\}` 称为映射 :math:`f` 的值域（`Range <http://mathworld.wolfram.com/Range.html>`_）

****
单射、满射和双射
****

设映射 :math:`f` 为一个从定义域 :math:`D` 到陪域 :math:`C` 的映射，

* 若对于定义域 :math:`D` 中任意原像 :math:`d_1`、:math:`d_2` 不等，对应像 :math:`f(d_1)`、:math:`f(d_2)` 恒不等，
  则称映射 :math:`f` 是单射（`Injection <http://mathworld.wolfram.com/Injection.html>`_）的。
* 若对于陪域 :math:`C` 中任一元素 :math:`c`像 :math:`y`，都存在原像 :math:`x` 使 :math:`f(x) = c`，
  则称映射 :math:`f` 是满射（`Surjection <http://mathworld.wolfram.com/Surjection.html>`_）的。
* 若映射 :math:`f` 既是单射的，又是满射的，
  则称映射 :math:`f` 是双射（`Bijection <http://mathworld.wolfram.com/Bijection.html>`_）的。

"""

__author__ = 'zhengrr'
