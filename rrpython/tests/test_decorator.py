#!/usr/bin/env python3
# coding: utf-8

r"""
装饰器。

即返回值为另一个函数的函数。

Notes
-----
- `装饰器 <https://docs.python.org/zh-cn/3/glossary.html#term-decorator>`_
"""
__version__ = '2020.11.04'
__since__ = '2018.11.04'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from typing import Any, Callable, overload


def decorator(function: Callable, /) -> Callable:
    r"""
    基础的装饰器，将函数原样返回。

    Examples
    --------
    >>> @decorator
    ... def rawer():
    ...     print('rawer is invoked.')
    ...
    decorator is invoked.
    >>> rawer()
    rawer is invoked.

    等价于

    >>> def rawer():
    ...     print('rawer is invoked.')
    ...
    >>> rawer = decorator(rawer)
    decorator is invoked.
    >>> rawer()
    rawer is invoked.
    """
    print('decorator is invoked.')
    return function


def decorator_return_wrapper(function: Callable, /) -> Callable:
    r"""
    使用闭包的装饰器，对传入函数进行包装，然后将该闭包返回。

    Examples
    --------
    >>> @decorator_return_wrapper
    ... def rawer():
    ...     print('rawer is invoked.')
    ...
    decorator is invoked.
    >>> rawer()
    wrapper is invoked.
    rawer is invoked.

    等价于

    >>> def rawer():
    ...     print('rawer is invoked.')
    ...
    >>> rawer = decorator_return_wrapper(rawer)
    decorator is invoked.
    >>> rawer()
    wrapper is invoked.
    rawer is invoked.
    """
    print('decorator is invoked.')

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print('wrapper is invoked.')
        return function(*args, **kwargs)

    return wrapper


def decorator_maker(mark: str = 'x') -> Callable[[Callable], Callable]:
    r"""
    装饰器的生成器。

    依据参数生成装饰器，生成的装饰器再对函数进行装饰，返回最终函数。

    Examples
    --------
    >>> @decorator_maker()
    ... def rawer():
    ...     print('rawer is invoked.')
    ...
    decorator maker is invoked.
    decorator with mark 'x' is invoked.
    >>> rawer()
    wrapper is invoked.
    rawer is invoked.

    等价于

    >>> def rawer():
    ...     print('rawer is invoked.')
    ...
    >>> decorator = decorator_maker()  # noqa
    decorator maker is invoked.
    >>> rawer = decorator(rawer)
    decorator with mark 'x' is invoked.
    >>> rawer()
    wrapper is invoked.
    rawer is invoked.
    """
    print('decorator maker is invoked.')

    def decorator(function: Callable) -> Callable:  # noqa
        print(f"decorator with mark '{mark}' is invoked.")

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print('wrapper is invoked.')
            return function(*args, **kwargs)

        return wrapper

    return decorator


@overload
def decorator_with_optional_parameter(function: Callable, /) -> Callable:
    ...


@overload
def decorator_with_optional_parameter(mark: str = 'x') -> Callable[[Callable], Callable]:
    ...


def decorator_with_optional_parameter(*args):
    r"""
    带可选参数的装饰器。

    在带有括号时，它是装饰器的生成器；在不带括号时，它是装饰器本身。

    Examples
    --------
    >>> @decorator_with_optional_parameter
    ... def rawer():
    ...     print('rawer is invoked.')
    ...
    decorator (maker) is invoked.
    decorator with mark 'x' is invoked.
    >>> rawer()
    wrapper is invoked.
    rawer is invoked.

    >>> @decorator_with_optional_parameter()
    ... def rawer():
    ...     print('rawer is invoked.')
    ...
    decorator (maker) is invoked.
    decorator with mark 'x' is invoked.
    >>> rawer()
    wrapper is invoked.
    rawer is invoked.

    >>> @decorator_with_optional_parameter('o')
    ... def rawer():
    ...     print('rawer is invoked.')
    ...
    decorator (maker) is invoked.
    decorator with mark 'o' is invoked.
    >>> rawer()
    wrapper is invoked.
    rawer is invoked.
    """
    print('decorator (maker) is invoked.')

    def decorator(function: Callable) -> Callable:  # noqa
        print(f"decorator with mark '{mark}' is invoked.")

        def wrapper(*args: Any, **kwargs: Any) -> Any:  # noqa
            print('wrapper is invoked.')
            return function(*args, **kwargs)

        return wrapper

    if len(args) == 1 and callable(args[0]):
        mark = 'x'
        return decorator(args[0])
    else:
        mark = args[0] if 0 < len(args) else 'x'
        return decorator
    pass


if __name__ == '__main__':
    from doctest import testmod

    testmod()
