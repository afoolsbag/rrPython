from functools import reduce


def factorial_recursive(n: int) -> int:
    r"""
    阶乘（使用递归方法）

    该函数受栈大小限制。
    """
    assert (0 < n)
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_tail_recursive(n: int, *, irp: int = 1) -> int:
    r"""
    阶乘（使用尾递归优化的递归方法）

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
    r"""
    阶乘（使用循环方法）
    """
    assert (0 < n)
    rv = 1
    while True:
        if n == 1:
            return rv
        n, rv = n - 1, rv * n


def fibonacci(m: int):
    r"""
    斐波那契数列生成器

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
    r"""
    装饰器工厂

    接受一些配置参数，返回一个装饰器。
    """

    def decorator(func):
        r"""
        装饰器（decorator）

        接受原始函数作为入参，返回包装函数作为出参。
        """

        def wrapper(*args, **kw):
            """
            包装函数（wrapper）

            调用原始函数，在其周围执行特定操作，返回原始函数返回的值。
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


def test_echo():
    echo('SMT, ZL, JT')


def test_map():
    r"""
    高阶函数 ``map``

    返回迭代器，惰性地对序列中的每一项调用指定函数并返值。
    """
    gen = map(lambda n: n ** 2, range(1, 4))
    assert next(gen) == 1
    assert next(gen) == 4
    assert next(gen) == 9


def test_filter():
    r"""
    高阶函数 ``filter``

    返回迭代器，惰性地对序列中的每一项调用指定函数判断真假，若为真则返回该项，若为假则尝试寻找下一项。
    """
    gen = filter(lambda n: n % 2 == 0, range(1, 5))
    assert next(gen) == 2
    assert 4, next(gen) == 4


def test_reduce():
    r"""
    高阶函数 ``reduce``

    使用指定函数，取出序列前两项进行运算，并将返回值插回序列头部；重复直至仅余一项，将其返回。

    .. note::

       Guido van Rossum 更倾向于使用 ``for`` 替代 ``reduce``::

          Removed reduce(). Use functools.reduce() if you really need it;
          however, 99 percent of the time an explicit for loop is more readable.
    """
    assert reduce(lambda x, y: x + y, range(1, 4)) == 6
