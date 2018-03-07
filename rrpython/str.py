#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    print('Unicode ord to chr: %s' % chr(0x8a00))
    print('Unicode chr to ord: %x' % ord('言'))

    print("UTF-8 to Unicode: %s" % b'\xe4\xb8\xad\xe6\x96\x87'.decode())
    print("Unicode to UTF-8: %s" % '中文'.encode())


if __name__ == '__main__':
    main()
