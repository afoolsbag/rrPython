#!/usr/bin/env python3
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt


def great_first_step():
    x = np.arange(1, 11)
    y = 2 * x + 5
    plt.title("GreatFirstStep demo")
    plt.xlabel("x axis caption")
    plt.ylabel("y axis caption")
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    great_first_step()
