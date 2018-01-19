#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-
def find_min_and_max(L):
    if 0 == len(L):
        return None, None
    min = max = L[0]
    for num in L:
        if num < min:
            min = num
        elif max < num:
            max = num
    return min, max


# 测试
if find_min_and_max([]) != (None, None):
    print('测试失败!')
elif find_min_and_max([7]) != (7, 7):
    print('测试失败!')
elif find_min_and_max([7, 1]) != (1, 7):
    print('测试失败!')
elif find_min_and_max([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
