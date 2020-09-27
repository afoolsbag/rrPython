#!/usr/bin/env python3
# coding: utf-8

r"""
可迭代类型。

::

    Iterable: obj.__iter__(self)  # iter(obj)

Notes
-----
- `可迭代类型 <https://docs.python.org/zh-cn/3/library/typing.html#typing.Iterable>`_
"""
__version__ = '2020.09.27'
__since__ = '2020.09.24'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from typing import Any, Iterable


def isiterable(obj: Any, /) -> bool:  # noqa
    r"""
    检查对象是否可迭代。

    有两类对象是可迭代的：

    - 支持迭代协议，具有 ``__iter__(self)`` 方法；
    - 支持序列协议，具有 ``__getitem__(self, key)`` 方法，且 ``key`` 从 ``0`` 开始。

    Parameters
    ----------
    obj : Any
        任意对象。

    Returns
    -------
    bool
        对象可迭代与否。
    """
    try:
        iter(obj)
        return True
    except TypeError:
        return False


def for_in_iterable(obj: Iterable, /) -> None:
    r"""
    可迭代对象可以通过 ``for ... in ...`` 语句进行迭代。
    """
    for item in obj:
        print(f'{item=}')


def for_in_enumerate_iterable(obj: Iterable, /) -> None:
    r"""
    可迭代对象可以通过 ``for ... in enumerate(...)`` 语句进行迭代。
    """
    for idx, item in enumerate(obj):
        print(f'{idx=} {item=}')


def all_iterable(obj: Iterable, /) -> bool:
    r"""
    可迭代对象的所有迭代返回值都为真时，返回真。
    """
    return all(obj)


def any_iterable(obj: Iterable, /) -> bool:
    r"""
    可迭代对象的任一迭代返回值为真时，返回真。
    """
    return any(obj)
