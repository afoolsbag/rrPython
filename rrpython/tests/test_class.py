#!/usr/bin/env python3
# coding: utf-8

__version__ = '2020.09.02'
__since__ = '2018.01.20'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from enum import Enum
from typing import Any


class MyClass(object):
    """类示例，默认继承自 ``object``"""

    __static_field: Any = None
    "类私有属性"

    __slots__ = ('__field',)

    def __init__(self):
        self.__field: Any = None
        "实例私有属性"

    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, value: Any):
        self.__field = value

    def __len__(self):
        """``len(object)`` """
        return len(self.__slots__)

    def __str__(self):
        """``str(object)`` """
        return 'Clazz instance with field=%s' % self.__field

    __repr__ = __str__


class MyEnum(Enum):
    Smt = 'Smt'
    Zl = 'Zl'
    Jt = 'Jt'


def test_instance():
    inst = MyClass()
    assert inst.field is None
