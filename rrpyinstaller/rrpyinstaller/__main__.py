#!/usr/bin/env python3
# coding: utf-8

r"""
使用 Python 构建命令行应用的示例项目。

Usage:
  rrpyinstaller [options]

  rrpyinstaller --test
  rrpyinstaller (-h | --help)
  rrpyinstaller --version

Options:
  -o --option=<opt>  Some option.

  --save             Save options to configuration file.

  --test             Test configurations and exit.
  -h --help          Show help message and exit.
  --version          Show version and exit.
"""
__version__ = '2020.09.18'
__since__ = '2020.08.17'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from dataclasses import dataclass

from loguru import logger

import rrpyinstaller
from rrpyinstaller.appaux import application_directory_path, BaseAppArgs, component_path, data_directory_path


@dataclass
class AppArgs(BaseAppArgs):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    option: str = 'default value'


@logger.catch
def main():
    # 日志
    logger.add(component_path(f'{rrpyinstaller.__name__}.log'), retention='1 week')

    # 参数
    args = AppArgs(source=component_path(f'{rrpyinstaller.__name__}.ini'),
                   doc=__doc__,
                   version=rrpyinstaller.__version__)

    # 业务逻辑
    print(f'Application directory path: {application_directory_path()}.')
    print(f'Data directory path: {data_directory_path()}.')


if __name__ == '__main__':
    main()
