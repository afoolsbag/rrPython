#!/usr/bin/env python3
# coding: utf-8

r"""
字节数组类型。

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
    +-> ByteString
    |
    bytearray

Notes
-----
- `字节数组类型 <https://docs.python.org/zh-cn/3/library/stdtypes.html#bytearray-objects>`_
"""
__version__ = '2020.09.26'
__since__ = '2020.09.26'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from typing import ByteString


def test_issubclass() -> None:
    assert issubclass(bytearray, ByteString)
