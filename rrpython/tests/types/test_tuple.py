#!/usr/bin/env python3
# coding: utf-8

r"""
元组类型。

::

            +-> Container: __contains__
            |
            +-> Sized: __len__
            |
            +-> Iterable: __iter__
            |
        +-> Collection
        |
        |   +-> Iterable: __iter__
        |   |
        +-> Reversible: __reversed__
        |
    +-> Sequence: __getitem__
    |             index
    |             count
    |
    Tuple
    tuple

Notes
-----
- `元组类型 <https://docs.python.org/zh-cn/3/library/stdtypes.html#tuples>`_
"""
__version__ = '2020.09.26'
__since__ = '2020.09.24'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from typing import Sequence


def test_issubclass() -> None:
    assert issubclass(tuple, Sequence)


def test_literal() -> None:
    v = ()
    assert isinstance(v, tuple)

    v = (1,)
    assert isinstance(v, tuple)

    v = (1, 2)
    assert isinstance(v, tuple)

    v = (1, 2, 3)
    assert isinstance(v, tuple)
