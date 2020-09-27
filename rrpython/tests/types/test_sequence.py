#!/usr/bin/env python3
# coding: utf-8

r"""
序列类型。

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
    Sequence: __getitem__
              count
              index

Notes
-----
- `序列类型 <https://docs.python.org/zh-cn/3/library/typing.html#typing.Sequence>`_
"""
__version__ = '2020.09.24'
__since__ = '2020.09.24'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from typing import Sequence


def for_in_range_len_sequence(obj: Sequence, /) -> None:
    r"""
    序列对象可以通过 ``for ... in range(len(...))`` 语句进行迭代。
    """
    for idx in range(len(obj)):
        print(f'{obj[idx]=}')
