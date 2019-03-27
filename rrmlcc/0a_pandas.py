#!/usr/bin/env python3
# coding: utf-8

"""
**学习目标**：

- 大致了解 pandas 库的 ``DataFrame`` 和 ``Series`` 数据结构
- 存取和处理 ``DataFrame`` 和 Series 中的数据
- 将 CSV 数据导入 pandas 库的 ``DataFrame``
- 对 ``DataFrame`` 重建索引来随机打乱数据

`pandas <http://pandas.pydata.org/>`_ 是一种列存数据分析 API。
它是用于处理和分析输入数据的强大工具，很多机器学习框架都支持将 pandas 数据结构作为输入。

虽然全方位介绍 pandas API 会占据很长篇幅，但它的核心概念非常简单，我们会在下文中进行说明。
有关更完整的参考，请访问 `pandas 文档网站 <http://pandas.pydata.org/pandas-docs/stable/index.html>`_，
其中包含丰富的文档和教程资源。
"""

import pandas as pd
import unittest as ut


class TestPandas(ut.TestCase):

    def test_pandas_version(self):
        """
        输出 pandas API 版本。
        """
        print('pandas version: %s' % pd.__version__)

    def test_data(self):
        """
        pandas 中的主要数据结构被实现为以下两类：

        ``DataFrame``
            可以将它想象成一个关系型数据表格，其中包含多个行和已命名的列。

        ``Series``
            它是单一列。`DataFrame` 中包含一个或多个 `Series`，每个 `Series` 均有一个名称。

        数据框架是用于数据操控的一种常用抽象实现形式。
        `Spark <https://spark.apache.org/>`_ 和 `R <https://r-project.org/>`_ 中也有类似的实现。

        """
        city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
        population = pd.Series([852469, 1015785, 485199])

        sheet = pd.DataFrame({'City name': city_names, 'Population': population})
        print(sheet)

    def test_load_csv(self):
        sheet = pd.read_csv('https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv', sep=',')
        print('describe:')
        print(sheet.describe())

        print('head:')
        print(sheet.head())

    def test_numpy(self):
        """
        `NumPy <http://www.numpy.org/>`_ 是一种用于进行科学计算的常用工具包。
        pandas ``Series`` 可用作大多数 NumPy 函数的参数。
        """


if __name__ == '__main__':
    ut.main()
