#!/usr/bin/env python3
# coding: utf-8

r"""
辅助工具。
"""

__version__ = '2020.09.02'
__since__ = '2020.08.17'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from os.path import abspath, dirname, join
import sys


def application_directory_path() -> str:
    r"""
    应用目录路径，即开发模式下项目根目录，或打包模式下可执行文件所在目录。
    """
    if getattr(sys, 'frozen', False):
        return dirname(abspath(sys.executable))
    else:
        return dirname(dirname(abspath(__file__)))


def component_path(relative_path: str) -> str:
    r"""
    相对于应用目录的路径。
    """
    return join(application_directory_path(), relative_path)


def data_directory_path() -> str:
    r"""
    数据目录路径，即开发模式下该文件所在目录，或打包模式下临时资源目录。
    """
    if getattr(sys, 'frozen', False):
        return abspath(join(sys._MEIPASS, 'data'))
    else:
        return join(dirname(dirname(abspath(__file__))), 'data')


def data_path(relative_path: str) -> str:
    r"""
    相对于数据目录的路径。
    """
    return join(data_directory_path(), relative_path)
