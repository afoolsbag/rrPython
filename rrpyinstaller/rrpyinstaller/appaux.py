#!/usr/bin/env python3
# coding: utf-8

r"""
应用辅助，提供常用基础设施。

Origin: https://github.com/afoolsbag/rrPython/blob/master/rrpyinstaller/rrpyinstaller/appaux.py
"""
__version__ = '2020.09.22'
__since__ = '2020.08.17'
__author__ = 'zhengrr'
__license__ = 'UNLICENSE'

from dataclasses import dataclass, fields
from distutils.util import strtobool
from os.path import abspath, dirname, join
from re import sub
import sys
from typing import Any, Dict, ItemsView, KeysView, List, Union, ValuesView

from docopt import docopt
from profig import Config


def application_directory_path() -> str:
    r"""
    应用目录路径，即开发模式下项目根目录，或打包模式下可执行文件所在目录。

    Returns
    -------
    str
        绝对路径。
    """
    if getattr(sys, 'frozen', False):
        return dirname(abspath(sys.executable))
    else:
        return dirname(dirname(abspath(__file__)))


def component_path(relative_path: str) -> str:
    r"""
    相对于应用目录的路径。

    Parameters
    ----------
    relative_path : str
        相对路径。

    Returns
    -------
    str
        绝对路径。
    """
    return join(application_directory_path(), relative_path)


def data_directory_path() -> str:
    r"""
    数据目录路径，即开发模式下该文件所在目录，或打包模式下临时资源目录。

    Returns
    -------
    str
        绝对路径。
    """
    if getattr(sys, 'frozen', False):
        return join(abspath(sys._MEIPASS), 'data')  # noqa
    else:
        return join(dirname(dirname(abspath(__file__))), 'data')


def data_path(relative_path: str) -> str:
    r"""
    相对于数据目录的路径。

    Parameters
    ----------
    relative_path : str
        相对路径。

    Returns
    -------
    str
        绝对路径。
    """
    return join(data_directory_path(), relative_path)


@dataclass
class BaseAppArgs:
    r"""
    基础应用参数类。
    从环境变量、配置文件、命令行等处解析参数，并提供相关功能。

    参数优先级由高到低依次为：
    1. 命令行参数
    2. 配置文件参数

    Warnings
    --------
    对于 ``docopt`` 中的开关选项而言，其始终解析为 ``bool`` 值，恒不为 ``None``，因而必然覆盖配置项。
    所以对于 ``bool`` 值，若希望持久化存储，应采用 ``--option=<bool>`` 的形式替代 ``--flag`` 的形式。

    子类定义的字段须要提供类型和默认值，否则可能报错。

    Examples
    --------
    >>> @dataclass
    >>> class AppArgs(BaseAppArgs):
    >>>     def __init__(self, *args, **kwargs):  # noqa
    >>>         super().__init__(*args, **kwargs)
    >>>
    >>>     option: str = 0
    >>>
    >>> args = AppArgs(source='path/to/config.ini', doc='docopt doc...', version='1.3.3.7')
    """

    @staticmethod
    def attrname(name: str) -> str:
        r"""
        将任意名称转换为属性名。
        """
        tmp = sub(r'[^\d\w]', '_', name).strip('_').lower()
        if not tmp:
            raise ValueError(f'The name can\'t convert to an attrname: "{name}".')
        if tmp[0:1].isdigit():
            tmp = '_' + tmp
        return tmp

    def __init__(self, *,
                 source: str, encoding: str = 'utf-8', strict: bool = True,
                 doc: str, version: Any):
        r"""
        初始化方法。

        Parameters
        ----------
        source : str
            profig 数据源路径，即配置文件路径。
        encoding : str
            profig 数据源编码。
        strict : bool
            profig 严格模式。
        doc : str
            docopt 所需文档。
        version : Any
            docopt 所需版本。
        """
        # ----------------------------------------------------------------------
        # 配置

        # 初始化 profig.Config 对象
        self.__profig: Config
        self.__profig = Config(source, encoding=encoding, strict=strict)
        for field in fields(self):
            self.__profig.init(f'global.{field.name}', getattr(self, field.name), field.type)
        self.__profig.sync()
        self.__sync_from_profig()

        # ----------------------------------------------------------------------
        # 命令

        # 调用 docopt.docopt 方法，提供了对 '-h'、'--help' 和 '--version' 参数的处理
        self.__docopt_dict: Dict[str, Union[bool, str, List[str], None]]
        self.__docopt_dict = docopt(doc, version=version)

        # 解析返回值，将符合条件的参数设置到字段
        docopt_key: str
        docopt_value: Union[bool, str, List[str], None]
        for docopt_key, docopt_value in self.__docopt_dict.items():
            if docopt_value is None:
                continue
            field_key = self.attrname(docopt_key)  # 规整化参数名
            for field in fields(self):
                if field.name != field_key:
                    continue
                if field.type is bool and isinstance(docopt_value, str):
                    setattr(self, field_key, field.type(strtobool(docopt_value)))  # 对 bool 类型参数需要特别处理
                else:
                    setattr(self, field_key, field.type(docopt_value))
                break

        # 对 '--save' 参数的处理
        if '--save' in self.__docopt_dict and self.__docopt_dict['--save']:
            self.save()

        # 对 '--test' 参数的处理
        if '--test' in self.__docopt_dict and self.__docopt_dict['--test']:
            print(self)
            print(self.__docopt_dict)
            sys.exit()

    def __sync_from_profig(self) -> None:
        r"""
        从 profig 同步到字段。
        """
        for field in fields(self):
            setattr(self, field.name, self.__profig[f'global.{field.name}'])

    def __sync_to_profig(self) -> None:
        r"""
        从字段同步到 profig。
        """
        for field in fields(self):
            self.__profig[f'global.{field.name}'] = getattr(self, field.name)

    def load(self) -> None:
        r"""
        从配置文件中加载配置。
        """
        self.__profig.read()
        self.__sync_from_profig()

    def save(self) -> None:
        r"""
        将配置保存到配置文件。
        """
        self.__sync_to_profig()
        self.__profig.write()

    def __getitem__(self, item: str) -> Union[bool, str, List[str], None]:
        r"""
        获取 docopt.docopt 返回的原始字典项。
        """
        return self.__docopt_dict[item]

    def items(self) -> ItemsView:
        r"""
        获取 docopt.docopt 返回的原始字典项的项视图。
        """
        return self.__docopt_dict.items()

    def keys(self) -> KeysView:
        r"""
        获取 docopt.docopt 返回的原始字典项的键视图。
        """
        return self.__docopt_dict.keys()

    def values(self) -> ValuesView:
        r"""
        获取 docopt.docopt 返回的原始字典项的值视图。
        """
        return self.__docopt_dict.values()

    def kwargs(self) -> Dict:
        r"""
        获取 docopt.docopt 返回的原始字典项，将其中的键规整化，以便于用作 ``**kwargs`` 参数。
        """
        tmp = {}
        for key, value in self.__docopt_dict.items():
            tmp[self.attrname(key)] = value
        return tmp
