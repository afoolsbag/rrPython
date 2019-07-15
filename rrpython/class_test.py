#!/usr/bin/env python3
# coding: utf-8

__author__ = 'zhengrr'

from enum import Enum
from typing import Any
import unittest


class MyClass:
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


class TestClass(unittest.TestCase):
    def test_instance(self):
        inst = MyClass()
        self.assertIsNone(inst.field)


if __name__ == '__main__':
    unittest.main()
