#!/usr/bin/env python3
# coding: utf-8

"""sci

####
集合
####

集合（`Set <http://mathworld.wolfram.com/Set.html>`_）
  简称集，指具有某种特定性质的事物的总体，常用大写拉丁字母表示，如集合 :math:`S`。

元素（`Element <http://mathworld.wolfram.com/Element.html>`_）
  即集合中的事物，常用小写拉丁字母表示，如元素 :math:`e`。

集合中的元素是无序的、互异的、确定的；
集合常以以下方式表示：

* 列举，如 :math:`\\mathbb{N} = \\{ 0, 1, 2, 3, \\ldots, n, \\ldots \\}`；
* 描述，如 :math:`\\mathbb{N}_+ = \\{ e | e \\text{ 是正整数 } \\}`；
* 文氏图（`Venn Diagram <http://mathworld.wolfram.com/VennDiagram.html>`_）。

****************
集合与元素的关系
****************

属于、拥有
  若元素 :math:`e` 是集合 :math:`S` 中的事物，称元素 :math:`e` 属于集合 :math:`S`，记作 :math:`e \\in S`；

  或称集合 :math:`S` 拥有元素 :math:`e`，记作 :math:`S \\ni e`。

不属于、不拥有
  若元素 :math:`e` 不是集合 :math:`S` 中的事物，称元素 :math:`e` 不属于集合 :math:`S`，记作 :math:`e \\notin S`；

  或称集合 :math:`S` 不拥有元素 :math:`e`，记作 :math:`S \\notni e`。

空集（`Empty Set <http://mathworld.wolfram.com/EmptySet.html>`_）
  不拥有任何元素的集合称作空集，记作 :math:`\\emptyset`。

全集（`Universe <http://mathworld.wolfram.com/UniversalSet.html>`_）
  在指定上下文中，拥有所有元素的集合称作全集，记作 :math:`U`。

****************
集合与集合的关系
****************

相等
  若集合 :math:`A` 和集合 :math:`B` 拥有的所有元素相同，称集合 :math:`A` 等于集合 :math:`B`，记作 :math:`A = B`；

  或称集合 :math:`B` 等于集合 :math:`A`，记作 :math:`B = A`。

包含于、包含
  若集合 :math:`S` 拥有的所有元素，集合 :math:`L` 都拥有，
  称集合 :math:`S` 包含于集合 :math:`L`，记作 :math:`S \\subseteq L`；

  或称集合 :math:`L` 包含集合 :math:`S`，记作 :math:`L \\supseteq S`；

  集合 :math:`S` 是集合 :math:`L` 的子集（`Subset <http://mathworld.wolfram.com/Subset.html>`_），
  集合 :math:`L` 是集合 :math:`S` 的超集（`Superset <http://mathworld.wolfram.com/Superset.html>`_）；

  :math:`(A \\subseteq B) \\equiv \\forall a (a \\in A \\implies a \\in B)`。

真包含于、真包含
  若集合 :math:`S` 拥有的所有元素，集合 :math:`L` 都拥有，且集合 :math:`L` 还拥有其他元素：

  称集合 :math:`S` 真包含于集合 :math:`L`，记作 :math:`S \\subset L`；

  或称集合 :math:`L` 真包含集合 :math:`S`，记作 :math:`L \\supseteq S`；

  集合 :math:`S` 是集合 :math:`L` 的真子集（`Proper Subset <http://mathworld.wolfram.com/ProperSubset.html>`_），
  集合 :math:`L` 是集合 :math:`S` 的真超集（`Proper Superset <http://mathworld.wolfram.com/ProperSuperset.html>`_）；

  :math:`(A \\subset B) \\equiv \\forall a (a \\in A \\implies a \\in B) \\land \\exists b(b \\in B \\land b \\notin A)`。

************
集合间的运算
************

并（`Cup <http://mathworld.wolfram.com/Cup.html>`_）
  将属于集合 :math:`A` 或属于集合 :math:`B` 的所有元素，划分成新的集合，称集合 :math:`A` 并集合 :math:`B`，记作 :math:`A \\cup B`；

  集合 :math:`A \\cup B` 是集合 :math:`A` 和集合 :math:`B` 的并集（`Union <http://mathworld.wolfram.com/Union.html>`_）；

  :math:`A \\cup B = \\{ e | e \\in A \\lor e \\in B \\}`。

  * 幺元 :math:`A \\cup \\emptyset = \\emptyset \\cup A = A`
  * 交换律 :math:`A \\cup B = B \\cup A`
  * 结合律 :math:`A \\cup (B \\cup C) == (A \\cup B) \\cup C`
  * 幂等律 :math:`A \\cup A = A`

交（`Cap <http://mathworld.wolfram.com/Cap.html>`_）
  将属于集合 :math:`A` 且属于集合 :math:`B` 的所有元素，划分成新的集合，称集合 :math:`A` 交集合 :math:`B`，记作 :math:`A \\cap B`；

  集合 :math:`A \\cap B` 是集合 :math:`A` 和集合 :math:`B` 的交集（`Intersection <http://mathworld.wolfram.com/Intersection.html>`_）；

  :math:`A \\cap B = \\{ e | e \\in A \\land e \\in B \\}`。

  * 零元 :math:`A \\cap \\emptyset = \\emptyset \\cap A = \\emptyset`
  * 交换律 :math:`A \\cap B = B \\cap A`
  * 结合律 :math:`A \\cap (B \\cap C) = (A \\cap B) \\cap C`
  * 幂等律 :math:`A \\cap A = A`

减（`Set Minus <http://mathworld.wolfram.com/SetMinus.html>`_）
  将属于集合 :math:`A` 但不属于集合 :math:`B` 的所有元素，划分成新的集合，成集合 :math:`A` 减集合 :math:`B`，记作 :math:`A \\setminus B`；

  集合 :math:`A \\setminus B` 是集合 :math:`B` 在集合 :math:`A` 中的差集（`Set Difference <http://mathworld.wolfram.com/SetDifference.html>`_）；

  :math:`A \\setminus B = \\{ e | e \\in A \\land e \\notin B \\}`。

  * 左零元 :math:`\\emptyset \\setminus A = \\emptyset`
  * 右幺元 :math:`A \\setminus \\emptyset = A`

补集（`Complement Set <http://mathworld.wolfram.com/ComplementSet.html>`_）
  若集合 :math:`L` 包含集合 :math:`S`，则属于集合 :math:`L` 但不属于集合 :math:`S` 的所有元素组成的集合，
  称超集 :math:`L` 中子集 :math:`S` 的补集，记作 :math:`\\complement{_{L}S}`；

  :math:`\\complement{_{L}S} = L \\setminus S`。

  特别的，若存在全集 :math:`U`，则属于全集 :math:`U` 但不属于集合 :math:`S` 的所有元素组成的集合，
  称集合 :math:`S` 的补集，记作 :math:`S^c`；

  :math:`S^c = U \\setminus S`。

  * 对偶律 :math:`(A \\cup B)^c = A^c \\cap B^c`，:math:`(A \\cap B)^c = A^c \\cup B^c`

对称差（`Symmetric Difference <http://mathworld.wolfram.com/SymmetricDifference.html>`_）
  属于集合 :math:`A` 或属于集合 :math:`B`，但不同时属于二者的所有元素组成的集合，
  称集合 :math:`A` 和集合 :math:`B` 的对称差，记作 :math:`A \\ominus B`；

  :math:`A \\ominus B = (A \\cup B) \\setminus (A \\cap B)`。

笛卡尔积（`Cartesian Product <http://mathworld.wolfram.com/CartesianProduct.html>`_）
  属于集合 :math:`A` 的元素，和属于集合 :math:`B` 的元素，组成的所有有序对作为元素，组成的集合，
  称集合 :math:`A` 和集合 :math:`B` 的笛卡尔积，记作 :math:`A \\times B`；

  :math:`A \\times B = \\{ (a, b) | a \\in A \\land b \\in B \\}`。

  特别的，集合 :math:`S \\times S` 称作集合 :math:`S` 的笛卡儿平方。

  * 零元 :math:`A \\times \\emptyset = \\emptyset \\times A = \\emptyset`

**************
若干命名的数集
**************

十六元数集 :math:`\\mathbb{S}`
八元数集 :math:`\\mathbb{O}`
四元数集 :math:`\\mathbb{H}`
复数集 :math:`\\mathbb{C}`
虚数集 :math:`\\mathbb{I}`
实数集 :math:`\\mathbb{R}`
正数集 :math:`\\mathbb{R}^+`
负数集 :math:`\\mathbb{R}^-`
无理数集
有理数集 :math:`\\mathbb{Q}`
分数集
整数集 :math:`\\mathbb{Z}`
负整数集 :math:`\\mathbb{Z}^-`
自然数集 :math:`\\mathbb{N}`
正整数集 :math:`\\mathbb{Z}^+`
素数集 :math:`\\mathbb{P}`

"""

__author__ = 'zhengrr'
