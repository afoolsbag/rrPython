#!/usr/bin/env python3
# coding: utf-8

r"""
字符串包装类型。

::

            +-> Container: obj.__contains__(self, item)  # item in obj
            |
            +-> Sized: obj.__len__(self)  # len(obj)
            |
            +-> Iterable: obj.__iter__(self)  # iter(obj)
            |
        +-> Collection
        |
        |   +-> Iterable: obj.__iter__(self)  # iter(obj)
        |   |
        +-> Reversible: obj.__reversed__(self)  # reversed(obj)
        |
    +-> Sequence: obj.__getitem__(self, index)  # obj[index]
    |             obj.count(self, value)
    |             obj.index(self, value, start=0, stop=None)
    |
    UserString

Notes
-----
- `字符串包装类型 <https://docs.python.org/zh-cn/3/library/collections.html#userstring-objects>`_
"""
__version__ = '2020.09.27'
__since__ = '2020.09.26'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from collections import UserString
from typing import Sequence


def test_issubclass() -> None:
    assert issubclass(UserString, Sequence)
