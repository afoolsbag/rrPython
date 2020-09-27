#!/usr/bin/env python3
# coding: utf-8

r"""
生成器类型。

::

        +-> Iterable: __iter__
        |
    +-> Iterator: __next__
    |
    Generator: close
               throw
               send

Notes
-----
- `生成器类型 <https://docs.python.org/zh-cn/3/library/typing.html#typing.Generator>`_
"""
__version__ = '2020.09.27'
__since__ = '2020.09.27'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from itertools import count
from typing import Generator


def fibonacci(max_: int) -> Generator[int, None, str]:
    r"""
    斐波那契数列（的生成器工厂）。

    Notes
    -----
    ::

        n=0: (0, 1), 1, 2, 3, 5, 8, 13, ...
              fn fm

        n=1: 0, (1, 1), 2, 3, 5, 8, 13, ...
                 fn fm

        n=2: 0, 1, (1, 2), 3, 5, 8, 13, ...
                    fn fm

    """
    n, fn, fm = 0, 0, 1
    while n < max_:
        yield fn
        fn, fm = fm, fn + fm
        n += 1

    return f'Fibonacci done with {max_=}.'


def test_literal() -> None:
    # with next

    v = fibonacci(7)
    assert isinstance(v, Generator)

    for n in count():
        try:
            fn = next(v)
            print(f'{n=} {fn=}')
        except StopIteration as e:
            print(f'{e=}', end='\n\n')
            break

    # with for ... in ...

    v = fibonacci(7)
    assert isinstance(v, Generator)

    for n, fn in enumerate(v):
        print(f'{n=} {fn=}')


if __name__ == '__main__':
    test_literal()
