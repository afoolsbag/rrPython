#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    tuple = ('zrr', 'love', 'smt', 'zl', 'jt')
    for str in tuple:
        print(str, end=' ')

    sum = 0
    for num in range(101):
        sum += num
    print(sum)

    while 0 < sum:
        sum -= 1337
        # continue
        # break
    print(sum)


if __name__ == '__main__':
    main()
