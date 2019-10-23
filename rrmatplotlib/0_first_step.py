#!/usr/bin/env python3
# coding: utf-8

__author__ = 'zhengrr'

import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
import numpy as np
import unittest


class TestFirstStep(unittest.TestCase):

    def test_empty_figure(self):
        """空画布"""
        fig = plt.figure()
        fig.suptitle('empty figure')
        fig.show()

    def test_axes_figure(self):
        """带轴的画布"""
        fig, ax = plt.subplots()
        fig.show()

    def test_pyplot_style(self):
        """pyplot 风格
        使用 pyplot 创建画布，然后使用 Axes 绘制 np 对象，最后展示画布"""
        pass

    def test_matlab_style(self):
        """MATLAB 风格"""
        pass

    def test_half_circle(self):
        fig, ax = plt.subplots()
        x = np.linspace(-1, 1, 100)
        y1 = np.sqrt(1 - np.square(x))
        y2 = -np.sqrt(1 - np.square(x))
        ax.plot(x, y1)
        ax.plot(x, y2)
        fig.show()

    def test_show(self):
        plt.show()


if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['SimHei']
    mplstyle.use('fast')
    unittest.main()
