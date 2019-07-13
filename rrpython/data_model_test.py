#!/usr/bin/env python3
# coding: utf-8

"""数据模型示例

.. seealso::

  - `Data model <https://docs.python.org/3/reference/datamodel.html>`_
"""
__author__ = 'zhengrr'

import unittest


class TestTheStandardTypeHierarchy(unittest.TestCase):
    """标准数据层次

    .. seealso::

      - `The standard type hierarchy
        <https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy>`_
      - `PEP 483 -- The Theory of Type Hints <https://python.org/dev/peps/pep-0483/>`_
      - `PEP 484 -- Type Hints <https://python.org/dev/peps/pep-0484/>`_
      - `PEP 526 -- Syntax for Variable Annotations <https://python.org/dev/peps/pep-0526/>`_
      - `typing — Support for type hints <https://docs.python.org/3/library/typing.html>`_
    """

    def test_none(self):
        """缺值"""
        eg: None = None
        self.assertFalse(eg)

    def test_not_implemented(self):
        """未实现"""
        eg: NotImplemented = NotImplemented
        self.assertTrue(eg)

    def test_ellipsis(self):
        """省略"""
        eg: Ellipsis = ...
        self.assertTrue(eg)

    def test_integer(self):
        """数字＞整数＞整型

        Python 中整型没有大小限制。
        """
        zero: int = 0
        self.assertFalse(zero)
        nonzero: int = 1
        self.assertTrue(nonzero)

        self.assertEqual(0b1, 1)
        self.assertEqual(0o7, 7)
        self.assertEqual(0xF, 15)

        self.assertEqual(3, 10 // 3)
        self.assertEqual(1, 10 % 3)

    def test_boolean(self):
        """数字＞整数＞布尔型"""
        false: bool = False
        self.assertFalse(false)
        true: bool = True
        self.assertTrue(true)

        self.assertFalse(True and False)
        self.assertTrue(True or False)
        self.assertFalse(not True)

    def test_real(self):
        """数字＞实数（浮点型）

        Python 中使用双精度浮点数存储实数。
        """
        zero: float = 0.
        self.assertFalse(zero)
        nonzero: float = 1.
        self.assertTrue(nonzero)

    def test_complex(self):
        """数字＞复数（双重浮点型）"""
        zero: complex = 0j
        self.assertFalse(zero)
        nonzero: complex = 1j
        self.assertTrue(nonzero)

    def test_string(self):
        """序列＞不变序列＞字符串"""
        empty: str = ''
        self.assertFalse(empty)
        nonempty: str = '1337'
        self.assertTrue(nonempty)

        self.assertEqual(65, ord('A'))
        self.assertEqual('A', chr(65))

        self.assertEqual(3, len('ABC'))

    def test_tuple(self):
        """序列＞不变序列＞元组"""
        empty: tuple = ()
        self.assertFalse(empty)
        nonempty: tuple = (1,)
        self.assertTrue(nonempty)

        tmp: tuple = ('0/-4', '1/-3', '2/-2', '3/-1')
        self.assertEqual('0/-4', tmp[0])
        self.assertEqual('3/-1', tmp[-1])

        # 切片
        tmp: tuple = (1, 3, 3, 7)
        self.assertTupleEqual((3, 3), tmp[1:3])
        self.assertTupleEqual((1, 3), tmp[:2])
        self.assertTupleEqual((3, 7), tmp[-2:])
        self.assertTupleEqual(tmp, tmp[:])
        self.assertTupleEqual((1, 3), tmp[::2])

        # 生成器
        gen = (x ** 2 for x in range(1, 4))
        self.assertEqual(1, next(gen))
        self.assertEqual(4, next(gen))
        self.assertEqual(9, next(gen))

    def test_bytes(self):
        """序列＞不变序列＞字节串"""
        empty: bytes = b''
        self.assertFalse(empty)
        nonempty: bytes = b'1337'
        self.assertTrue(nonempty)

        self.assertEqual('ABC', b'ABC'.decode('ASCII'))
        self.assertEqual(b'ABC', 'ABC'.encode('UTF-8'))

        self.assertEqual(3, len(b'ABC'))

        self.assertEqual('ABC, XYZ', '%s, %s' % ('ABC', 'XYZ'))
        self.assertEqual('ABC, XYZ', '{0}, {1}'.format('ABC', 'XYZ'))

    def test_list(self):
        """序列＞可变序列＞列表"""
        empty: list = []
        self.assertFalse(empty)
        nonempty: list = [1, 3, 3, 7]
        self.assertTrue(nonempty)

        # 列表生成式
        self.assertListEqual([1, 2, 3], [x for x in range(1, 4)])
        self.assertListEqual([1, 4, 9], [x ** 2 for x in range(1, 4)])

    def test_bytearray(self):
        """序列＞可变序列＞字节数组"""
        empty: bytearray = bytearray(b'')
        self.assertFalse(empty)
        nonempty: bytearray = bytearray(b'1337')
        self.assertTrue(nonempty)

    def test_set(self):
        """集合＞集合"""
        empty: set = set()
        self.assertFalse(empty)
        nonempty: set = {1, 3, 3, 7}
        self.assertTrue(nonempty)

        self.assertEqual(3, len({1, 3, 3, 7}))
        self.assertSetEqual({3}, {1, 3} & {3, 7})
        self.assertSetEqual({1, 3, 7}, {1, 3} | {3, 7})

    def test_frozenset(self):
        """集合＞冻结集合"""
        empty: frozenset = frozenset()
        self.assertFalse(empty)
        nonempty: frozenset = frozenset({1, 3, 3, 7})
        self.assertTrue(nonempty)

    def test_dictionary(self):
        """映射＞字典

        Python 中字典的 Key 必须是不变对象
        """
        empty: dict = {}
        self.assertFalse(empty)
        nonempty: dict = {'key': 'value'}
        self.assertTrue(nonempty)

        self.assertTrue('key' in {'key': 'value'})


if __name__ == '__main__':
    unittest.main()
