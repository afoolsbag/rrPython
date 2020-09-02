#!/usr/bin/env python3
# coding: utf-8

__version__ = '2020.09.02'
__since__ = '2018.01.20'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

import random


def test_if():
    if random.randint(0, 1):
        pass
    elif random.randint(0, 1):
        pass
    else:
        pass


def test_for_in():
    for x in range(10):
        print('x:', x)


TD = {'kSMT': 'vSMT', 'kZL': 'vZl', 'kJT': 'vJT'}


def test_for_in_dict_key():
    for key in TD:
        print('key:', key)


def test_for_in_dict_value():
    for value in TD.values():
        print('value:', value)


def test_for_in_dict_pair():
    for key, value in TD.items():
        print('key:', key, 'value:', value)


def test_for_in_dict_index():
    for index, value in enumerate(TD):
        print('index:', index, 'value:', value)


def test_while():
    while random.randint(0, 1):
        pass
