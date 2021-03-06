#!/usr/bin/env python3
# coding: utf-8

r"""
字典包装类型。

::

                +-> Container: __contains__
                |
                +-> Sized: __len__
                |
                +-> Iterable: __iter__
                |
            +-> Collection
            |
        +-> Mapping: __eq__
        |            __getitem__
        |            __ne__
        |            get
        |            items
        |            keys
        |            values
        |
    +-> MutableMapping: __delitem__
    |                   __setitem__
    |                   clear
    |                   pop
    |                   popitem
    |                   setdefault
    |                   update
    |
    UserDict

Notes
-----
- `字典包装类型 <https://docs.python.org/zh-cn/3/library/collections.html#userdict-objects>`_
"""
__version__ = '2020.09.26'
__since__ = '2020.09.26'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from collections import UserDict
from typing import MutableMapping


def test_issubclass() -> None:
    assert issubclass(UserDict, MutableMapping)
