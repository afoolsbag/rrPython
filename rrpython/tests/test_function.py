#!/usr/bin/env python3
# coding: utf-8

r"""
.. seealso::

   - `Function definitions <https://docs.python.org/reference/compound_stmts.html#function-definitions>`_

   - `PEP 483 -- The Theory of Type Hints <https://python.org/dev/peps/pep-0483/>`_
   - `PEP 484 -- Type Hints <https://python.org/dev/peps/pep-0484/>`_
   - `PEP 3107 -- Function Annotations <https://python.org/dev/peps/pep-3107/>`_
   - `typing — Support for type hints <https://docs.python.org/3/library/typing.html>`_
"""
__version__ = '2020.09.02'
__since__ = '2018.01.20'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from typing import Any, Tuple


def empty() -> None:
    r"""
    空函数
    """
    pass


def test_empty():
    empty()


def with_positional_parameters(positional_argument_1: Any,
                               positional_argument_2: Any,
                               positional_argument_3: Any = 'default value') -> None:
    r"""
    带位置参数的函数

    .. note::

       Python 中函数参数默认值必须是不变对象。

    :param positional_argument_1: 位置参数 1
    :param positional_argument_2: 位置参数 2
    :param positional_argument_3: 位置参数 3
    """
    print('positional argument 1 = ', positional_argument_1)
    print('positional argument 2 = ', positional_argument_2)
    print('positional argument 3 = ', positional_argument_3)


def test_with_positional_parameters():
    with_positional_parameters('SMT', 'ZL', 'JT')


def with_variadic(*args: Any) -> None:
    r"""
    带可变参数的函数

    :param args: 可变参数（arguments）
    """
    print('args:', args)


def test_with_variadic():
    with_variadic('SMT', 'ZL', 'JT')
    with_variadic(*('SMT', 'ZL', 'JT'))
    with_variadic(*['SMT', 'ZL', 'JT'])


def with_named_parameters(*,
                          named_argument_1: Any,
                          named_argument_2: Any,
                          named_argument_3: Any = 'default value') -> None:
    r"""
    带具名参数的函数

    .. note::

       Python 中函数参数默认值必须是不变对象。

    :param named_argument_1: 具名参数 1
    :param named_argument_2: 具名参数 2
    :param named_argument_3: 具名参数 3
    """
    print('named arguments 1:', named_argument_1)
    print('named arguments 2:', named_argument_2)
    print('named arguments 3:', named_argument_3)


def test_with_named_parameters():
    with_named_parameters(named_argument_1='SMT', named_argument_2='ZL', named_argument_3='JT')


def with_keyword_parameters(**kwargs: Any) -> None:
    r"""
    带键值参数的函数

    :param kwargs: 键值参数（keyword-value arguments）
    """
    print('kwargs:', kwargs)


def test_with_keyword_parameters():
    with_keyword_parameters(k1='SMT', k2='ZL', k3='JT')
    with_keyword_parameters(**{'k1': 'SMT', 'k2': 'ZL', 'k3': 'JT'})


def all_in_one(positional_argument_1: Any,
               positional_argument_2: Any,
               positional_argument_3: Any = 'default value',
               *args: Any,
               named_argument_1: Any,
               named_argument_2: Any,
               named_argument_3: Any = 'default value',
               **kwargs: Any) -> None:
    print('positional argument 1 = ', positional_argument_1)
    print('positional argument 2 = ', positional_argument_2)
    print('positional argument 3 = ', positional_argument_3)
    print('args:', args)
    print('named arguments 1:', named_argument_1)
    print('named arguments 2:', named_argument_2)
    print('named arguments 3:', named_argument_3)
    print('kwargs:', kwargs)


def with_multi_return() -> Tuple[str, str, str]:
    r"""
    带多值返回的函数

    .. note::

       实际返回的仍然是一个值，一个包含多个值的元组（tuple）。
    """
    return 'SMT', 'ZL', 'JT'


def test_with_multi_return():
    smt, zl, jt = with_multi_return()
    assert smt == 'SMT'
    assert zl == 'ZL'
    assert jt == 'JT'
