#!/usr/bin/env python3
# coding: utf-8

r"""
命名元组类型。

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
    +-> Tuple
    |
    NamedTuple

Notes
-----
- `命名元组类型 <https://docs.python.org/zh-cn/3/library/collections.html#namedtuple-factory-function-for-tuples-with-named-fields>`_
"""
__version__ = '2020.09.27'
__since__ = '2020.09.26'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from collections import namedtuple


def test_issubclass() -> None:
    Point3D = namedtuple('Point3D', ['x', 'y', 'z'])
    assert issubclass(Point3D, tuple)
