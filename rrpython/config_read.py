#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser

config = configparser.ConfigParser()
config.read('config.ini')
print(config.get('section', 'key', fallback='default'))


def main():
    pass


if __name__ == '__main__':
    main()
