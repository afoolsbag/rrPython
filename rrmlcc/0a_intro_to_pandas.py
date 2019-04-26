#!/usr/bin/env python3
# coding: utf-8

"""
- `前提条件和准备工作 <https://developers.google.com/machine-learning/crash-course/prereqs-and-prework>`_

- `Pandas 简介 <https://colab.research.google.com/notebooks/mlcc/intro_to_pandas.ipynb>`_
"""

import numpy as np
import pandas as pd
import unittest as ut


class TestCase(ut.TestCase):

    def test_version(self):
        """
        - `pandas <http://pandas.pydata.org/>`_
        - `pandas 文档 <http://pandas.pydata.org/pandas-docs/stable/>`_
        """
        print('pandas version: %s' % pd.__version__)

    def test_data_types(self):
        """
        列（``Series``）和框（``Frame``）

        - `《二〇一八年全国姓名报告》权威发布 <http://news.cpd.com.cn/n18151/201901/t20190130_830962.html>`_
        - `pandas 索引和选择 <http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html>`_
        """
        family_names = pd.Series(['王', '李', '张', '刘', '陈', '杨', '黄', '赵', '吴', '周'])
        people_counts = pd.Series([1.015, 1.009, 0.954, 0.721, 0.633, 0.462, 0.337, 0.286, 0.278, 0.268])
        sheet = pd.DataFrame({'姓氏': family_names, '人数（亿人）': people_counts})

        print('《二〇一八年全国姓名报告》框')
        print(sheet)
        print()

        print('"姓氏"列')
        print(sheet['姓氏'])
        print()

        print('第一行')
        print(sheet[0:1])
        print()

    def test_read_from_csv(self):
        """
        从 csv 文件中读取数据
        """
        california_housing_sheet = pd.read_csv(
            'https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv', sep=',')

        print('统计信息')
        print(california_housing_sheet.describe())
        print()

        print('头部数行')
        print(california_housing_sheet.head())
        print()

    def test_numpy(self):
        """
        - `NumPy <http://www.numpy.org/>`_
        """
        nums = pd.Series([852469, 1015785, 485199])
        print('nums')
        print(nums)
        print()

        logs = np.log(nums)
        print('logs')
        print(logs)
        print()

        mils = nums.apply(lambda val: 1000000 < val)
        print('mils')
        print(mils)
        print()


if __name__ == '__main__':
    ut.main()
