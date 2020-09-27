#!/usr/bin/env python3
# coding: utf-8

r"""
字典类型。

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
    Dict
    dict

Notes
-----
- `字典类型 <https://docs.python.org/zh-cn/3/library/stdtypes.html#mapping-types-dict>`_
"""
__version__ = '2020.09.26'
__since__ = '2020.09.26'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from typing import MutableMapping


def test_issubclass() -> None:
    assert issubclass(dict, MutableMapping)


def test_literal() -> None:
    v = {}
    assert isinstance(v, dict)

    v = {1: 1}
    assert isinstance(v, dict)

    v = {1: 1, 2: 2}
    assert isinstance(v, dict)

    v = {1: 1, 2: 2, 3: 3}
    assert isinstance(v, dict)
