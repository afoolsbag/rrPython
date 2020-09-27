#!/usr/bin/env python3
# coding: utf-8

r"""
计数器类型。

::

                        +-> Container: obj.__contains__(self, item)  # item in obj
                        |
                        +-> Sized: obj.__len__(self)  # len(obj)
                        |
                        +-> Iterable: obj.__iter__(self)  # iter(obj)
                        |
                    +-> Collection
                    |
                +-> Mapping: obj.__eq__(self. rhv)       # obj == rhv
                |            obj.__getitem__(self, key)  # obj[key]
                |            obj.__ne__(self, rhv)       # obj != rhv
                |            obj.get(self, key, default=None)
                |            obj.items(self)
                |            obj.keys(self)
                |            obj.values(self)
                |
            +-> MutableMapping: obj.__delitem__(self, key)         # del obj[key]
            |                   obj.__setitem__(self, key, value)  # obj[key] = value
            |                   obj.clear(self)
            |                   obj.pop(self, key, default=__marker)
            |                   obj.popitem(self)
            |                   obj.setdefault(self, key, default=None)
            |                   obj.update(self, other=(), /, **kwds)
            |
        +-> Dict
        |
    +-> Counter
    |
    Counter

Notes
-----
- `计数器类型 <https://docs.python.org/zh-cn/3/library/collections.html#counter-objects>`_
"""
__version__ = '2020.09.27'
__since__ = '2020.09.26'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from collections import Counter
from typing import Counter as CounterT


def test_issubclass() -> None:
    assert issubclass(Counter, CounterT)
