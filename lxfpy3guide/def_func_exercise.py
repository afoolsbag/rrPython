#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def quadratic(a, b, c):
    if 0 == a and 0 == b:
        return '无解'
    if 0 == a:
        return -c / b
    _delta = b * b - 4 * a * c
    if _delta < 0:
        return '无解'
    _x1 = (-b + math.sqrt(_delta)) / (2 * a)
    _x2 = (-b - math.sqrt(_delta)) / (2 * a)
    return _x1, _x2


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
