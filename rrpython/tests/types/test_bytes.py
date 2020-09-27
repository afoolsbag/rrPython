#!/usr/bin/env python3
# coding: utf-8

r"""
字节串类型。

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
    bytes

Notes
-----
- `字节串类型 <https://docs.python.org/zh-cn/3/library/stdtypes.html#bytes-objects>`_
"""
__version__ = '2020.09.26'
__since__ = '2020.09.24'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from typing import ByteString


def test_issubclass() -> None:
    assert issubclass(bytes, ByteString)