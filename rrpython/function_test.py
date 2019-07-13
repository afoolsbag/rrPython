#!/usr/bin/env python3
# coding: utf-8

__author__ = 'zhengrr'

from functools import reduce
from typing import Any, Tuple
import unittest


def nop() -> None:
    """空函数

    .. seealso::

      - `PEP 483 -- The Theory of Type Hints <https://python.org/dev/peps/pep-0483/>`_
      - `PEP 484 -- Type Hints <https://python.org/dev/peps/pep-0484/>`_
      - `PEP 3107 -- Function Annotations <https://python.org/dev/peps/pep-3107/>`_
      - `typing — Support for type hints <https://docs.python.org/3/library/typing.html>`_
    """
    pass


def w_pos_param(pa1: Any, pa2: Any, pa3: Any = 'default value') -> None:
    """带位置参数（的函数）：(function) with positional parameter

    .. note::

      Python 中函数参数默认值必须是不变对象。

    :param pa1: 位置参数 1：positional argument 1
    :param pa2: 位置参数 2：positional argument 2
    :param pa3: 位置参数 3：positional argument 3
    """
    print('pa1:', pa1, 'pa2:', pa2, 'pa3:', pa3)


def w_variadic(*args: Any) -> None:
    """带可变参数（的函数）：(function) with variadic

    :param args：可变参数：arguments
    """
    print('args:', args)


def w_named_param(*, na1: Any, na2: Any, na3: Any = 'default value') -> None:
    """带具名参数（的函数）：(function) with named parameter

    .. note::

      Python 中函数参数默认值必须是不变对象。

    :param na1: 具名参数 1：named argument 1
    :param na2: 具名参数 2：named argument 2
    :param na3: 具名参数 3：named argument 3
    """
    print('na1:', na1, 'na2:', na2, 'na3:', na3)


def w_keyword_param(**kw: Any) -> None:
    """带键值参数（的函数）：(function) with keyword parameter

    :param kw：键值参数：keyword (-value) argument
    """
    print('kw:', kw)


def w_multi_return() -> Tuple[str, str, str]:
    """多值返回"""
    return 'SMT', 'ZL', 'JT'


def all_in_one(pa1: Any, pa2: Any, pa3: Any = 'default value', *args: Any,
               na1: Any, na2: Any, na3: Any = 'default value', **kw: Any):
    print('pa1:', pa1, 'pa2:', pa2, 'pa3:', pa3)
    print('args:', args)
    print('na1:', na1, 'na2:', na2, 'na3:', na3)
    print('kw:', kw)


def factorial_recursive(n: int) -> int:
    """阶乘：使用递归方法

    该函数受栈大小限制。
    """
    assert (0 < n)
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_tail_recursive(n: int, *, irp: int = 1) -> int:
    """阶乘：使用尾递归优化的递归方法

    Python 不支持尾递归优化，该函数仍受栈大小限制。

    :param n: 数
    :param irp: 内部保留参数（internal reserved parameter），如果不知它有何作用，就不要变动它
    :return: 数的阶乘
    """
    assert (0 < n)
    assert (0 < irp)
    if n == 1:
        return irp
    return factorial_tail_recursive(n - 1, irp=irp * n)


def factorial_loop(n: int) -> int:
    """阶乘：使用循环方法"""
    assert (0 < n)
    rv = 1
    while True:
        if n == 1:
            return rv
        n, rv = n - 1, rv * n


def fibonacci(m: int):
    """斐波那契数列生成器

    可迭代（``Iterable``）和迭代器（``Iterator``）::

      - 可迭代表示该对象可用于``for-in``循环；
      - 迭代器表示该对象是惰性计算序列。
    """
    assert (0 < m)
    i, p, v = 0, 0, 1  # i: current index; p: previous value; v: current value
    while i < m:
        yield v
        i, p, v = i + 1, v, v + p
    return 'fibonacci generator return value, can get by StopIteration exception'


def print_call(pretext: str = 'print_call'):
    """装饰器工厂

    接受一些配置参数，返回一个装饰器。
    """

    def decorator(func):
        """装饰器：decorator

        接受原始函数作为入参，返回包装函数作为出参。
        """

        def wrapper(*args, **kw):
            """包装函数：wrapper

            调用原始函数，在其周围执行特定操作，返回值。
            """
            print('%s: enter %s(%s, %s):' % (pretext, func.__name__, args, kw))
            rv = func(*args, **kw)
            print('%s: leave %s(%s, %s).' % (pretext, func.__name__, args, kw))
            return rv

        return wrapper

    return decorator


@print_call()
def echo(message):
    print('echo:', message)


class TestFunction(unittest.TestCase):

    def test_nop(self):
        nop()

    def test_w_pos_param(self):
        w_pos_param('SMT', 'ZL', 'JT')

    def test_w_variadic(self):
        w_variadic('SMT', 'ZL', 'JT')
        w_variadic(*('SMT', 'ZL', 'JT'))
        w_variadic(*['SMT', 'ZL', 'JT'])

    def test_w_named_param(self):
        w_named_param(na1='SMT', na2='ZL', na3='JT')

    def test_w_keyword_param(self):
        w_keyword_param(k1='SMT', k2='ZL', k3='JT')
        w_keyword_param(**{'k1': 'SMT', 'k2': 'ZL', 'k3': 'JT'})

    def test_w_multi_return(self):
        smt, zl, jt = w_multi_return()
        self.assertEqual('SMT', smt)
        self.assertEqual('ZL', zl)
        self.assertEqual('JT', jt)

    def test_map(self):
        """高阶函数 ``map``

        返回迭代器，惰性地对序列中的每一项调用指定函数并返值。
        """
        gen = map(lambda n: n ** 2, range(1, 4))
        self.assertEqual(1, next(gen))
        self.assertEqual(4, next(gen))
        self.assertEqual(9, next(gen))

    def test_filter(self):
        """高阶函数 ``filter``

        返回迭代器，惰性地对序列中的每一项调用指定函数判断真假，若为真则返回该项，若为假则尝试寻找下一项。
        """
        gen = filter(lambda n: n % 2 == 0, range(1, 5))
        self.assertEqual(2, next(gen))
        self.assertEqual(4, next(gen))

    def test_reduce(self):
        """高阶函数 ``reduce``

        使用指定函数，取出序列前两项进行运算，并将返回值插回序列头部；重复直至仅余一项，将其返回。

        .. note::

          Guido van Rossum 更倾向于使用 ``for`` 替代 ``reduce``::

            Removed reduce(). Use functools.reduce() if you really need it;
            however, 99 percent of the time an explicit for loop is more readable.
        """
        self.assertEqual(6, reduce(lambda x, y: x + y, range(1, 4)))

    def test_echo(self):
        echo('SMT, ZL, JT')


if __name__ == '__main__':
    unittest.main()
