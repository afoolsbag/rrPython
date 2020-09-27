#!/usr/bin/env python3
# coding: utf-8

r"""
冻结集合类型。

::

                +-> Container: obj.__contains__(self, item)  # item in obj
                |
                +-> Sized: obj.__len__(self)  # len(obj)
                |
                +-> Iterable: obj.__iter__(self)  # iter(obj)
                |
            +-> Collection
            |
        +-> AbstractSet: obj.__and__(self, rhv)   # obj & rhv
        |                obj.__eq__(self, rhv)    # obj == rhv
        |                obj.__ge__(self, rhv)    # obj >= rhv
        |                obj.__gt__(self, rhv)    # obj > rhv
        |                obj.__le__(self, rhv)    # obj <= rhv
        |                obj.__lt__(self, rhv)    # obj < rhv
        |                obj.__ne__(self, rhv)    # obj != rhv
        |                obj.__or__(self, rhv)    # obj | rhv
        |                obj.__rand__(self, lhv)  # lhv & obj
        |                obj.__ror__(self, lhv)   # lhv | obj
        |                obj.__rsub__(self, lhv)  # lhv - obj
        |                obj.__rxor__(self, lhv)  # lhv ^ obj
        |                obj.__sub__(self, rhv)   # obj - rhv
        |                obj.__xor__(self, rhv)   # obj ^ rhv
        |                obj.isdisjoint(self, other)
        |
    +-> FrozenSet
    |
    frozenset

Notes
-----
- `冻结集合类型 <https://docs.python.org/zh-cn/3/library/stdtypes.html#set-types-set-frozenset>`_
"""
__version__ = '2020.09.27'
__since__ = '2020.09.24'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from typing import FrozenSet


def test_issubclass() -> None:
    assert issubclass(frozenset, FrozenSet)


def test_literal() -> None:
    v = frozenset()
    assert isinstance(v, frozenset)

    v = frozenset({1, 2, 3})
    assert isinstance(v, frozenset)
