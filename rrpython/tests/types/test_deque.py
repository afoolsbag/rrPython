#!/usr/bin/env python3
# coding: utf-8

r"""
双端队列类型。

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
    +-> MutableSequence: __setitem__
    |                    __delitem__
    |                    __iadd__
    |                    insert
    |                    append
    |                    reverse
    |                    extend
    |                    pop
    |                    remove
    |
    Deque
    deque

Notes
-----
- `双端队列类型 <https://docs.python.org/zh-cn/3/library/collections.html#deque-objects>`_
"""
__version__ = '2020.09.26'
__since__ = '2020.09.26'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from collections import deque
from typing import MutableSequence


def test_issubclass() -> None:
    assert issubclass(deque, MutableSequence)
