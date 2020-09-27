#!/usr/bin/env python3
# coding: utf-8

r"""
序列类型。

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
    Sequence: obj.__getitem__(self, index)  # obj[index]
              obj.count(self, value)
              obj.index(self, value, start=0, stop=None)

Notes
-----
- `序列类型 <https://docs.python.org/zh-cn/3/library/typing.html#typing.Sequence>`_
"""
__version__ = '2020.09.27'
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
