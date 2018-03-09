#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    dict = {'smt': 2, 'zl': 3, 'jt': 2}
    for word in dict:
        print('%s: %d' % (word, dict[word]))

    poi = {'smt', 'zl', 'jt'}
    w2d = {'smt', 'jt'}
    w3d = {'zl'}

    print(poi & w2d)
    print(poi & w3d)


if __name__ == '__main__':
    main()
