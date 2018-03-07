#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    list = ['smt', 'zl', 'jt']
    tuple = ('smt', 'zl', 'jt')

    # 访问
    print('tuple[0]: %s' % tuple[0])
    print('tuple[-1]: %s' % tuple[-1])

    # 插入、附加、删除
    list.insert(0, 'love')
    list.append('rbq')
    list.pop()


if __name__ == '__main__':
    main()
