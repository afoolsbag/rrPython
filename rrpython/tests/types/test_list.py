#!/usr/bin/env python3
# coding: utf-8

r"""
列表类型。

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
        +-> MutableSequence: obj.__delitem__(self, index)         # del obj[index]
        |                    obj.__iadd__(self, rhv)              # obj += rhv
        |                    obj.__setitem__(self, index, value)  # obj[index] = value
        |                    obj.append(self, value)
        |                    obj.extend(self, values)
        |                    obj.insert(self, index, value)
        |                    obj.pop(self, index=-1)
        |                    obj.remove(self, value)
        |                    obj.reverse(self)
        |
    +-> List
    |
    list

Notes
-----
- `列表类型 <https://docs.python.org/zh-cn/3/library/stdtypes.html#lists>`_
"""
__version__ = '2020.09.27'
__since__ = '2020.09.24'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from typing import MutableSequence


def test_issubclass() -> None:
    assert issubclass(list, MutableSequence)


def test_literal() -> None:
    v = []
    assert isinstance(v, list)

    v = [1]
    assert isinstance(v, list)

    v = [1, 2]
    assert isinstance(v, list)

    v = [1, 2, 3]
    assert isinstance(v, list)
