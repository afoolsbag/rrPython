#!/usr/bin/env python3
# coding: utf-8

"""sci

####
集合论
####

集合（`Set <http://mathworld.wolfram.com/Set.html>`_）
  简称集，指具有某种特定性质的事物的总体，常用大写拉丁字母表示，如集合 :math:`S`。

元素（`Element <http://mathworld.wolfram.com/Element.html>`_）
  即集合中的事物，常用小写拉丁字母表示，如元素 :math:`e`。

****
集合与元素
****

属于
  若元素 :math:`e` 是集合 :math:`S` 中的事物，称元素 :math:`e` 属于集合 :math:`S`，记作
* 若元素 :math:`e` 是集合 :math:`S` 的成员，记作 :math:`e \\in S` （元素 :math:`e` 属于集合 :math:`S`），

  或 :math:`S \\ni e` （拥有）。

* 若元素 :math:`e` 不是集合 :math:`S` 的成员，
  记作 :math:`e \\notin S` （不属于），
  或 :math:`S \\notni e` （不拥有）。

* 不拥有任何元素的集合称作空集（`Empty Set <http://mathworld.wolfram.com/EmptySet.html>`_），
  记作 :math:`\\emptyset`。

* 在指定上下文中，拥有所有元素的集合称作全集（`Universe <http://mathworld.wolfram.com/UniversalSet.html>`_），
  记作 :math:`U`。

****
集合与集合
****

* 若集合 :math:`A` 和集合 :math:`B` 拥有的元素完全相同，
  记作 :math:`A = B` （等于）。

* 若集合 :math:`V` 拥有的所有元素，集合 :math:`W` 都拥有，
  记作 :math:`V \\subseteq W` （包含于），
  或 :math:`W \\supseteq V` （包含），
  集合 :math:`V` 是集合 :math:`W` 的子集（`Subset <http://mathworld.wolfram.com/Subset.html>`_），
  集合 :math:`W` 是集合 :math:`V` 的超集（`Superset <http://mathworld.wolfram.com/Superset.html>`_）。

* 若集合 :math:`V` 拥有的所有元素，集合 :math:`W` 都拥有，且集合 :math:`W` 还拥有其他元素，
  记作 :math:`V \\subset W` （真包含于），
  或 :math:`W \\supset V` （真包含），
  集合 :math:`V` 是集合 :math:`W` 的真子集（`Proper Subset <http://mathworld.wolfram.com/ProperSubset.html>`_），
  集合 :math:`W` 是集合 :math:`V` 的真超集（`Proper Superset <http://mathworld.wolfram.com/ProperSuperset.html>`_）。

****
集合的运算
****

* 属于集合 :math:`A` 或属于集合 :math:`B` 的所有元素组成的集合，
  记作 :math:`A \\cup B` （并（`Cup <http://mathworld.wolfram.com/Cup.html>`_）），
  集合 :math:`A \\cup B` 是集合 :math:`A` 和集合 :math:`B` 的并集（`Union <http://mathworld.wolfram.com/Union.html>`_），
  :math:`A \\cup B = \\{ e | e \\in A \\lor e \\in B \\}`。

* 属于集合 :math:`A` 且属于集合 :math:`B` 的所有元素组成的集合，
  记作 :math:`A \\cap B` （交（`Cap <http://mathworld.wolfram.com/Cap.html>`_）），
  集合 :math:`A \\cap B` 是集合 :math:`A` 和集合 :math:`B` 的交集（`Intersection <http://mathworld.wolfram.com/Intersection.html>`_），
  :math:`A \\cap B = \\{ e | e \\in A \\land e \\in B \\}`。

* 属于集合 :math:`A` 但不属于集合 :math:`B` 的所有元素组成的集合，
  记作 :math:`A \\setminus B` （减（`Set Minus <http://mathworld.wolfram.com/SetMinus.html>`_）），
  集合 :math:`A \\setminus B` 是集合 :math:`B` 在集合 :math:`A` 中的差集（`Set Difference <http://mathworld.wolfram.com/SetDifference.html>`_），
  :math:`A \\setminus B = \\{ e | e \\in A \\land e \\notin B \\}`。

* 特别的，若 :math:`W` 包含 :math:`V`，则属于 :math:`V` 但不属于 :math:`W` 的所有元素组成的集合，
  记作 :math:`\\complement{_{W}V}`，读作“超集Ｗ中子集Ｖ的补集（`Complement Set <http://mathworld.wolfram.com/ComplementSet.html>`_）”

* 特别的，若存在全集，则属于 :math:`U` 但不属于 :math:`S` 的所有元素组成的集合，
  记作 :math:`S^C`，读作“集合Ｓ的补集”。

.. math::

  \frac{ }{N}

"""

__author__ = 'zhengrr'
