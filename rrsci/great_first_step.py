#!/usr/bin/env python3
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np


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
