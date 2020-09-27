#!/usr/bin/env python3
# coding: utf-8

r"""
范围类型。

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
    |             count
    |             index
    |
    range

Notes
-----
- `范围类型 <https://docs.python.org/zh-cn/3/library/stdtypes.html#ranges>`_
"""
__version__ = '2020.09.26'
__since__ = '2020.09.24'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from typing import Sequence


def test_issubclass() -> None:
    assert issubclass(range, Sequence)


def test_literal() -> None:
    v = range(1337)
    assert isinstance(v, range)

    v = range(0, 1337, 1)
    assert isinstance(v, range)
