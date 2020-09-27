#!/usr/bin/env python3
# coding: utf-8

r"""
复数类型。

::

        +-> Number
        |
    +-> Complex: obj.__abs__(self)            # abs(obj)
    |            obj.__add__(self, rhv)       # obj + rhv
    |            obj.__bool__(self)           # bool(obj)
    |            obj.__complex__(self)        # complex(obj)
    |            obj.__eq__(self, rhv)        # obj == rhv
    |            obj.__mul__(self, rhv)       # obj * rhv
    |            obj.__ne__(self, rhv)        # obj != rhv
    |            obj.__neg__(self)            # -obj
    |            obj.__pos__(self)            # +obj
    |            obj.__pow__(self, rhv)       # obj ** rhv
    |            obj.__radd__(self, lhv)      # lhv + obj
    |            obj.__rmul__(self, lhv)      # lhv * obj
    |            obj.__rpow__(self, lhv)      # lhv ** obj
    |            obj.__rsub__(self, lhv)      # lhv - obj
    |            obj.__rtruediv__(self, lhv)  # lhv / obj
    |            obj.__sub__(self, rhv)       # obj - rhv
    |            obj.__truediv__(self, rhv)   # obj / rhv
    |            obj.conjugate(self)
    |            obj.imag(self)
    |            obj.real(self)
    |
    complex

Notes
-----
- `复数类型 <https://docs.python.org/zh-cn/3/library/stdtypes.html#numeric-types-int-float-complex>`_
"""
__version__ = '2020.09.27'
__since__ = '2020.09.27'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from numbers import Complex


def test_issubclass() -> None:
    assert issubclass(complex, Complex)


def test_literal() -> None:
    v = 0j
    assert isinstance(v, complex)

    v = 0 + 0j
    assert isinstance(v, complex)
