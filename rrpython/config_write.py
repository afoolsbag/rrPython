#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser

config = configparser.ConfigParser()
config['section'] = {'key': 'value',
                     'key2': 'value2',
                     'key3': 'value3'}
with open('config.ini', 'w') as configfile:
    config.write(configfile)
