#!/usr/bin/env python3
# coding: utf-8

r"""
实数类型。

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
    +-> Real: obj.__ceil__(self)                 # math.ceil(obj)
    |         obj.__divmod__(self, rhv)          # divmod(obj, rhv)
    |         obj.__floor__(self)                # math.floor(obj)
    |         obj.__floordiv__(self, rhv)        # obj // rhv
    |         obj.__float__(self)                # float(obj)
    |         obj.__ge__(self, rhv)              # obj >= rhv
    |         obj.__gt__(self, rhv)              # obj > rhv
    |         obj.__le__(self, rhv)              # obj <= rhv
    |         obj.__lt__(self, rhv)              # obj < rhv
    |         obj.__mod__(self, rhv)             # obj % rhv
    |         obj.__rdivmod__(self, lhv)         # divmod(lhv, obj)
    |         obj.__rfloordiv__(self, lhv)       # lhv // obj
    |         obj.__rmod__(self, lhv)            # lhv % obj
    |         obj.__round__(self, ndigits=None)  # round(obj, ndigits=None)
    |         obj.__trunc__(self)                # math.trunc(obj)
    |
    float

Notes
-----
- `实数类型 <https://docs.python.org/zh-cn/3/library/stdtypes.html#numeric-types-int-float-complex>`_
"""
__version__ = '2020.09.27'
__since__ = '2020.09.27'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from numbers import Real


def test_issubclass() -> None:
    assert issubclass(float, Real)
