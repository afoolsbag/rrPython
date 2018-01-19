#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def create_counter():
    cnt = 0

    def counter():
        nonlocal cnt
        cnt += 1
        return cnt

    return counter


# 测试:
counterA = create_counter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = create_counter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
