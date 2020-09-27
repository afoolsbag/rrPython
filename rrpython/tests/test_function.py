#!/usr/bin/env python3
# coding: utf-8

r"""
函数。

Notes
-----
- `函数定义 <https://docs.python.org/zh-cn/3/reference/compound_stmts.html#function-definitions>`_
"""
__version__ = '2020.09.24'
__since__ = '2018.01.20'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from typing import Any, Dict, Tuple


def function(pos: Any, /, std: Any, *args: Any, kwd: Any, **kwargs: Any) -> Tuple:
    r"""
    函数定义。

    Parameters
    ----------
    pos : Any
        “仅位置参数”，仅可通过位置传参。
    std : Any
        “标准参数”，可通过位置或关键字传参。
    args : Tuple[Any]
        “其余位置参数”。
    kwd : Any
        “仅关键字参数”，仅可通过关键字传参。
    kwargs : Dict[str, Any]
        “其余关键字参数”。

    Returns
    -------
    Tuple
        将参数值原样返回。
    """
    assert isinstance(args, Tuple)
    assert isinstance(kwargs, Dict)
    return pos, std, args, kwd, kwargs


def arguments_unpacked() -> None:
    r"""
    参数解包。

    使用 ``*(...)`` 或 ``*[...]`` 将元组或列表解包为位置参数；
    使用 ``**{...}`` 将字典解包为关键字参数。
    """
    pass
