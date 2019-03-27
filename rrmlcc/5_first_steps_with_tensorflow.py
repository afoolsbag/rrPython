#!/usr/bin/env python3
# coding: utf-8

"""

监督式机器学习：

1. 通过直觉，假定若干现象具有相关性（如假定某上市公司在某时的股票、财报、发布、新闻、国内政策和国际形势之间具有相关性）
2. 收集样本
3. 通过直觉，划分标签和特征（如将平均股价划为标签，将其他划为特征。问题：如何将特征量化？）
4. 通过直觉，选择损失函数（如 L2 损失函数）
5. 通过直觉，选择模型，设定初始参数（如线性回归模型）
6. 通过直觉，选择训练方法，设定超参数（如小批量随机梯度下降法）

使用 TensorFlow 的基本步骤

学习目标：

- 学习基本的 TensorFlow 概念
- 在 TensorFlow 中使用 ``LinearRegressor`` 类并基于单个输入特征预测各城市街区的房屋价值中位数
- 使用均方根误差 (RMSE) 评估模型预测的准确率
- 通过调整模型的超参数提高模型准确率

数据基于加利福尼亚州 1990 年的人口普查数据。

"""

# 首先，我们将加载必要的库。

import numpy as np
import pandas as pd
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

# 接下来，我们将加载数据集。

california_housing_dataframe = pd.read_csv(
    'https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv',
    sep=',')

# 我们将对数据进行随机化处理，以确保不会出现任何病态排序结果（可能会损害随机梯度下降法的效果）。
# 此外，我们会将 `median_house_value` 调整为以千为单位，这样，模型就能够以常用范围内的学习速率较为轻松地学习这些数据。

california_housing_dataframe = california_housing_dataframe.reindex(
    np.random.permutation(california_housing_dataframe.index))
california_housing_dataframe['median_house_value'] /= 1000.0
print(california_housing_dataframe)

# 检查数据
#
# 建议您在使用数据之前，先对它有一个初步的了解。
#
# 我们会输出关于各列的一些实用统计信息快速摘要：样本数、均值、标准偏差、最大值、最小值和各种分位数。
print(california_housing_dataframe.describe())

# TODO: ...
