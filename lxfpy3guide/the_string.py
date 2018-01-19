#!/usr/bin/env python3
# -*- coding: utf-8 -*-

bstr = '你好'.encode('utf-8')
print(bstr)

ustr = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print(ustr)

s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
