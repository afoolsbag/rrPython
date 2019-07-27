#!/usr/bin/env python3
# coding: utf-8

"""sci

####
映射
####

设集合 :math:`X` 和集合 :math:`Y` 是两个非空集合，
对于集合 :math:`X` 中任一元素 :math:`x`，依照某种规律 :math:`f`，恒有集合 :math:`Y` 中唯一确定元素 :math:`y` 与之对应，
则称对应规律 :math:`f` 为一个从集合 :math:`X` 到集合 :math:`Y` 的映射（`Map <http://mathworld.wolfram.com/Map.html>`_），
记作 :math:`f: X \\to Y` 或 :math:`f: x \\mapsto y`。
其中

* 集合 :math:`X` 称为映射 :math:`f` 的定义域（`Domain <http://mathworld.wolfram.com/Domain.html>`_）
* 集合 :math:`Y` 称为映射 :math:`f` 的陪域（`Codomain <http://mathworld.wolfram.com/Codomain.html>`_）
* 元素 :math:`x` 称为在映射 :math:`f` 下，元素 :math:`y` 的原像（`Preimage <http://mathworld.wolfram.com/Preimage.html>`_）
* 元素 :math:`y` 称为在映射 :math:`f` 下，元素 :math:`x` 的像（`Image <http://mathworld.wolfram.com/Image.html>`_），记作 :math:`y = f(x)`
* 集合 :math:`R_f = \\{ f(x) | x \\in X \\}` 称为映射 :math:`f` 的值域（`Range <http://mathworld.wolfram.com/Range.html>`_）

****************
单射、满射和双射
****************

设映射 :math:`f` 为一个从定义域 :math:`D` 到陪域 :math:`C` 的映射，

* 若对于定义域 :math:`D` 中任意原像 :math:`d_1`、:math:`d_2` 不等，对应像 :math:`f(d_1)`、:math:`f(d_2)` 恒不等，
  则称映射 :math:`f` 是单射（`Injection <http://mathworld.wolfram.com/Injection.html>`_）的。
* 若对于陪域 :math:`C` 中任一元素 :math:`c`像 :math:`y`，都存在原像 :math:`d` 使 :math:`f(d) = c`，
  则称映射 :math:`f` 是满射（`Surjection <http://mathworld.wolfram.com/Surjection.html>`_）的。
* 若映射 :math:`f` 既是单射的，又是满射的，
  则称映射 :math:`f` 是双射（`Bijection <http://mathworld.wolfram.com/Bijection.html>`_）的。

************************
逆映射、复合映射和函数幂
************************

逆映射（`Inverse Function <http://mathworld.wolfram.com/InverseFunction.html>`_）
  若映射 :math:`f: x \\mapsto y` 是双射的，
  则称映射 :math:`y \\mapsto x` 为映射 :math:`f` 的逆映射，记作 :math:`f^{-1}`。

复合映射（`Composition <http://mathworld.wolfram.com/Composition.html>`_）
  设存在映射 :math:`f: X \\to Y` 和映射 :math:`g: Y \\to Z`，
  则称映射 :math:`x \\mapsto g(f(x))` 为映射 :math:`f` 和映射 :math:`g` 的复合映射，记作 :math:`g \\circ f`。

函数幂
  若映射可与自身复合，则记 :math:`f \\circ f = f^2`、:math:`f \\circ f \\circ f = f^3`……

  若映射可逆，且逆映射可与其自身复合，则记 :math:`f^{-2} = (f^{-1})^2 = f^{-1} \\circ f^{-1}`……

  映射 :math:`f^0` 定义为定义域上的恒同映射。

********
二元运算
********

集合 :math:`S` 的笛卡儿平方 :math:`S \\times S` 到集合 :math:`S` 的映射 :math:`f: S \\times S \\to S`，
称作集合 :math:`S` 上的二元运算（`Binary Operation <http://mathworld.wolfram.com/BinaryOperation.html>`_）；
元素 :math:`a`、:math:`b` 是集合 :math:`S` 的元素，通常将 :math:`f(a, b)` 记作 :math:`a f b`。

设集合 :math:`S` 上的二元运算 :math:`*: S \\times S \\to S`，元素 :math:`e_0`、:math:`e_1` 是集合 :math:`S` 的元素：

零元（`Zero Element <http://mathworld.wolfram.com/ZeroElement.html>`_）
  若 :math:`\\forall a \\in S \\implies e_0 * a = e_0`，则称元素 :math:`e_0` 为二元运算 :math:`*` 的左零元；

  若 :math:`\\forall a \\in S \\implies a * e_0 = e_0`，则称元素 :math:`e_0` 为二元运算 :math:`*` 的右零元；

  若元素 :math:`e_0` 既是左零元又是右零元，则称其为零元。

幺元（`Identity Element <http://mathworld.wolfram.com/IdentityElement.html>`_）
  若 :math:`\\forall a \\in S \\implies e_1 * a = a`，则称元素 :math:`e_1` 为二元运算 :math:`*` 的左幺元；

  若 :math:`\\forall a \\in S \\implies a * e_1 = a`，则称元素 :math:`e_1` 为二元运算 :math:`*` 的右幺元；

  若元素 :math:`e` 既是左幺元又是右幺元，则称其为幺元。

交换律（`Commutative <http://mathworld.wolfram.com/Commutative.html>`_）
  若 :math:`\\forall a, b \\in S \\implies a * b = b * a`，则称二元运算 :math:`*` 满足交换律。

结合律（`Associative <http://mathworld.wolfram.com/Associative.html>`_）
  若 :math:`\\forall a, b, c \\in S \\implies (a * b) * c = a * (b * c)`，则称二元运算 :math:`*` 满足结合律。

幂等律
  若 :math:`\\forall a \\in S \\implies a * a = a`，则称二元运算 :math:`*` 满足幂等律。

幂零律
  若 :math:`\\forall a \\in S \\implies a * a = e_0`，则称二元运算 :math:`*` 满足幂零律。

幂幺律
  若 :math:`\\forall a \\in S \\implies a * a = e_1`，则称二元运算 :math:`*` 满足幂幺律。

"""

__author__ = 'zhengrr'
