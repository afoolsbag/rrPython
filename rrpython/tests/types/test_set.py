#!/usr/bin/env python3
# coding: utf-8

r"""
集合类型。

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
    +-> MutableSet: __iand__
    |               __ior__
    |               __isub__
    |               __ixor__
    |               add
    |               clear
    |               discard
    |               pop
    |               remove
    |
    Set
    set

Notes
-----
- `集合类型 <https://docs.python.org/zh-cn/3/library/stdtypes.html#set-types-set-frozenset>`_
"""
__version__ = '2020.09.26'
__since__ = '2020.09.26'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from typing import MutableSet


def test_issubclass() -> None:
    assert issubclass(set, MutableSet)


def test_literal() -> None:
    v = set()
    assert isinstance(v, set)

    v = {1}
    assert isinstance(v, set)

    v = {1, 2}
    assert isinstance(v, set)

    v = {1, 2, 3}
    assert isinstance(v, set)
