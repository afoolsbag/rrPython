#!/usr/bin/env python3
# coding: utf-8

__author__ = 'zhengrr'

import logging
import unittest


class TestException(unittest.TestCase):
    """异常

    .. seealso::

      - `Exception hierarchy
        <https://docs.python.org/3/library/exceptions.html#exception-hierarchy>`_
    """

    def test_except(self):
        try:
            pass
        except Exception as e:
            logging.exception(e)
        finally:
            pass

    def test_raise(self):
        with self.assertRaises(Exception):
            raise Exception('a test exception')


if __name__ == '__main__':
    unittest.main()
