#!/usr/bin/env python3
# coding: utf-8

__author__ = 'zhengrr'

from os import remove
from py import path


def test_write_read_file(tmpdir: path):
    tmp_file_path = tmpdir.join('test.txt')

    f1 = None
    try:
        f1 = open(tmp_file_path, 'w')
        f1.write('hello, world')
    finally:
        if f1:
            f1.close()

    with open(tmp_file_path, 'r') as f2:
        print(f2.read(1024))

    remove(tmp_file_path)
