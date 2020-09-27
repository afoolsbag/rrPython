#!/usr/bin/env python3
# coding: utf-8

r"""
列表类型。

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
    +-> MutableSequence: __delitem__
    |                    __iadd__
    |                    __setitem__
    |                    append
    |                    extend
    |                    insert
    |                    pop
    |                    remove
    |                    reverse
    |
    List
    list

Notes
-----
- `列表类型 <https://docs.python.org/zh-cn/3/library/stdtypes.html#lists>`_
"""
__version__ = '2020.09.24'
__since__ = '2020.09.24'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from typing import MutableSequence


def test_issubclass() -> None:
    assert issubclass(list, MutableSequence)


def test_literal() -> None:
    v = []
    assert isinstance(v, list)

    v = [1]
    assert isinstance(v, list)

    v = [1, 2]
    assert isinstance(v, list)

    v = [1, 2, 3]
    assert isinstance(v, list)
