#!/usr/bin/env python3
# coding: utf-8

"""
* 集合（`Set <http://mathworld.wolfram.com/Set.html>`_），简称集，常用大写拉丁字母表示，

  如 :math:`S`，读作“集合Ｓ”。

* 集合的成员称作元素（`Element <http://mathworld.wolfram.com/Element.html>`_），常用小写拉丁字母表示，

  如 :math:`e`，读作“元素ｅ”。

**集合与元素**

* 若 :math:`e` 是 :math:`S` 的元素，

  记作 :math:`e \\in S`，读作“元素ｅ属于集合Ｓ”；

  也可记作 :math:`S \\ni e`，读作“集合Ｓ拥有元素ｅ”。

* 若 :math:`e` 不是 :math:`S` 的元素，

  记作 :math:`e \\notin S`，读作“元素ｅ不属于集合Ｓ”；

  也可记作 :math:`S \\notni e`，读作“集合Ｓ不拥有元素ｅ”。

* 不拥有任何元素的集合称作空集（`Empty Set <http://mathworld.wolfram.com/EmptySet.html>`_），

  记作 :math:`\\emptyset`。

* 在指定上下文中，拥有所有元素的集合称作全集（Universe），

  记作 :math:`U`。

**集合与集合**

* 若 :math:`A` 和 :math:`B` 拥有的元素完全一样，

  记作 :math:`A = B`，读作“集合Ａ等于集合Ｂ”。

* 若 :math:`V` 拥有的所有元素，:math:`W` 都具有，

  记作 :math:`V \\subseteq W`，读作“集合Ｖ包含于集合Ｗ”或“集合Ｖ是集合Ｗ的子集”；

  也可记作 :math:`W \\supseteq V`，读作“集合Ｗ包含集合Ｖ”或“集合Ｗ是集合Ｖ的超集”。

* 若 :math:`V` 是 :math:`W` 的子集，且 :math:`V` 不等于 :math:`W`，

  记作 :math:`V \\subset W`，读作“集合Ｖ真包含于集合Ｗ”或“集合Ｖ是集合Ｗ的真子集”；

  也可记作 :math:`W \\supset V`，读作“集合Ｗ真包含集合Ｖ”或“集合Ｗ是集合Ｖ的真超集”。

**集合的运算**

* 属于 :math:`A` 或属于 :math:`B` 的所有元素组成的集合，

  记作 :math:`A \\cup B`，读作“集合Ａ和集合Ｂ的并集”，该运算读作“集合Ａ并集合Ｂ”：

  .. math::

    A \\cup B = \\{ e | e \\in A \\text{或} e \\in B \\}

* 属于 :math:`A` 且属于 :math:`B` 的所有元素组成的集合，

  记作 :math:`A \\cap B`，读作“集合Ａ和集合Ｂ的交集”，该运算读作“集合Ａ交集合Ｂ”。

* 属于 :math:`A` 但不属于 :math:`B` 的所有元素组成的集合，

  记作 :math:`A \\setminus B`，读作“集合Ｂ在集合Ａ中的差集”，该运算读作“集合Ａ减集合Ｂ”。

* 特别的，若 :math:`W` 包含 :math:`V`，则属于 :math:`V` 但不属于 :math:`W` 的所有元素组成的集合，

  记作 :math:`\\complement{_{W}V}`，读作“超集Ｗ中子集Ｖ的补集”。

* 特别的，若存在全集，则属于 :math:`U` 但不属于 :math:`S` 的所有元素组成的集合，

  记作 :math:`S^C`，读作“集合Ｓ的补集”。

.. math::

  \frac{ }{N}

"""

__author__ = 'zhengrr'
