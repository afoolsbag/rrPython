#!/usr/bin/env python3
# coding: utf-8

r"""
列表包装类型。

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
    UserList

Notes
-----
- `列表包装类型 <https://docs.python.org/zh-cn/3/library/collections.html#userlist-objects>`_
"""
__version__ = '2020.09.26'
__since__ = '2020.09.26'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from collections import UserList
from typing import MutableSequence


def test_issubclass() -> None:
    assert issubclass(UserList, MutableSequence)
