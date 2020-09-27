#!/usr/bin/env python3
# coding: utf-8

r"""
命名元组类型。

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
        Tuple
    +-> tuple
    |
    NamedTuple

Notes
-----
- `命名元组类型 <https://docs.python.org/zh-cn/3/library/collections.html#namedtuple-factory-function-for-tuples-with-named-fields>`_
"""
__version__ = '2020.09.26'
__since__ = '2020.09.26'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from collections import namedtuple


def test_issubclass() -> None:
    Point3D = namedtuple('Point3D', ['x', 'y', 'z'])
    assert issubclass(Point3D, tuple)
