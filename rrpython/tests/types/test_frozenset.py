#!/usr/bin/env python3
# coding: utf-8

r"""
冻结集合类型。

::

            +-> Container: __contains__
            |
            +-> Sized: __len__
            |
            +-> Iterable: __iter__
            |
        +-> Collection
        |
    +-> AbstractSet: __and__
    |                __eq__
    |                __ge__
    |                __gt__
    |                __le__
    |                __lt__
    |                __ne__
    |                __or__
    |                __sub__
    |                __xor__
    |                isdisjoint
    |
    FrozenSet
    frozenset

Notes
-----
- `冻结集合类型 <https://docs.python.org/zh-cn/3/library/stdtypes.html#set-types-set-frozenset>`_
"""
__version__ = '2020.09.26'
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
