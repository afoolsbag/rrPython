#!/usr/bin/env python3
# coding: utf-8

r"""
.. seealso::

   - `Data model <https://docs.python.org/reference/datamodel.html>`_
   - `The standard type hierarchy
     <https://docs.python.org/reference/datamodel.html#the-standard-type-hierarchy>`_

   - `PEP 483 -- The Theory of Type Hints <https://python.org/dev/peps/pep-0483/>`_
   - `PEP 484 -- Type Hints <https://python.org/dev/peps/pep-0484/>`_
   - `PEP 526 -- Syntax for Variable Annotations <https://python.org/dev/peps/pep-0526/>`_
   - `typing — Support for type hints <https://docs.python.org/3/library/typing.html>`_
"""
__version__ = '2020.09.02'
__since__ = '2018.01.20'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'


def test_none():
    r"""
    缺值
    """
    eg: None = None
    assert bool(eg) is False


def test_not_implemented():
    r"""
    未实现
    """
    eg: NotImplemented = NotImplemented
    assert bool(eg) is True


def test_ellipsis():
    r"""
    省略
    """
    eg: Ellipsis = ...
    assert bool(eg) is True


def test_integer():
    r"""
    数字 > 整数 > 整型

    Python 中整型没有大小限制。
    """
    zero: int = 0
    assert bool(zero) is False
    nonzero: int = 1
    assert bool(nonzero) is True

    assert 0b1 == 1
    assert 0o7 == 7
    assert 0xF == 15

    assert 10 // 3 == 3
    assert 10 % 3 == 1


def test_boolean():
    r"""
    数字 > 整数 > 布尔型
    """
    false: bool = False
    assert false is False
    true: bool = True
    assert true is True

    assert True and False is False
    assert True or False is True
    assert (not True) is False


def test_real():
    r"""
    数字 > 实数（浮点型）

    Python 中使用双精度浮点数存储实数。
    """
    zero: float = 0.
    assert bool(zero) is False
    nonzero: float = 1.
    assert bool(nonzero) is True


def test_complex():
    r"""
    数字 > 复数（双重浮点型）
    """
    zero: complex = 0j
    assert bool(zero) is False
    nonzero: complex = 1j
    assert bool(nonzero) is True


def test_string():
    r"""
    序列 > 不变序列 > 字符串
    """
    empty: str = ''
    assert bool(empty) is False
    nonempty: str = '1337'
    assert bool(nonempty) is True

    assert ord('A') == 65
    assert chr(65) == 'A'

    assert len('ABC') == 3


def test_tuple():
    r"""
    序列 > 不变序列 > 元组
    """
    empty: tuple = ()
    assert bool(empty) is False
    nonempty: tuple = (1,)
    assert bool(nonempty) is True

    tmp: tuple = ('0/-4', '1/-3', '2/-2', '3/-1')
    assert tmp[0] == '0/-4'
    assert tmp[-1] == '3/-1'

    # 切片
    tmp: tuple = (1, 3, 3, 7)
    assert tmp[1:3] == (3, 3)
    assert tmp[:2] == (1, 3)
    assert tmp[-2:] == (3, 7)
    assert tmp[:] == tmp
    assert tmp[::2] == (1, 3)

    # 生成器
    gen = (x ** 2 for x in range(1, 4))
    assert next(gen) == 1
    assert next(gen) == 4
    assert next(gen) == 9


def test_bytes():
    r"""
    序列 > 不变序列 > 字节串
    """
    empty: bytes = b''
    assert bool(empty) is False
    nonempty: bytes = b'1337'
    assert bool(nonempty) is True

    assert b'ABC'.decode('ASCII') == 'ABC'
    assert 'ABC'.encode('UTF-8') == b'ABC'

    assert len(b'ABC') == 3

    assert '%s, %s' % ('ABC', 'XYZ') == 'ABC, XYZ'
    assert '{0}, {1}'.format('ABC', 'XYZ') == 'ABC, XYZ'


def test_list():
    r"""
    序列 > 可变序列 > 列表
    """
    empty: list = []
    assert bool(empty) is False
    nonempty: list = [1, 3, 3, 7]
    assert bool(nonempty) is True

    # 列表生成式
    assert [x for x in range(1, 4)] == [1, 2, 3]
    assert [x ** 2 for x in range(1, 4)] == [1, 4, 9]


def test_bytearray():
    r"""
    序列 > 可变序列 > 字节数组
    """
    empty: bytearray = bytearray(b'')
    assert bool(empty) is False
    nonempty: bytearray = bytearray(b'1337')
    assert bool(nonempty) is True


def test_set():
    r"""
    集合 > 集合
    """
    empty: set = set()
    assert bool(empty) is False
    nonempty: set = {1, 3, 3, 7}
    assert bool(nonempty) is True

    assert len({1, 3, 3, 7}) == 3
    assert {1, 3} & {3, 7} == {3}
    assert {1, 3} | {3, 7} == {1, 3, 7}


def test_frozenset():
    r"""
    集合 > 冻结集合
    """
    empty: frozenset = frozenset()
    assert bool(empty) is False
    nonempty: frozenset = frozenset({1, 3, 3, 7})
    assert bool(nonempty) is True


def test_dictionary():
    r"""
    映射 > 字典

    Python 中字典（dictionary）的键（key）必须是不变对象
    """
    empty: dict = {}
    assert bool(empty) is False
    nonempty: dict = {'key': 'value'}
    assert bool(nonempty) is True

    assert ('key' in {'key': 'value'}) is True
