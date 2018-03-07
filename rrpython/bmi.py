#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    print('Body Mass Index')
    mass = float(input('Your mass (kg): '))
    height = float(input('Your height (m): '))
    bmi = mass / (height ** 2)

    print('Your BMI is %g' % bmi)

    print('世界卫生组织（WHO）：', end='')
    if bmi < 15:
        print('非常严重的体重不足')
    elif bmi < 16:
        print('严重体重不足')
    elif bmi < 18.5:
        print('体重不足')
    elif bmi < 25:
        print('健康的体重')
    elif bmi < 30:
        print('超重')
    elif bmi < 35:
        print('中度肥胖')
    elif bmi < 40:
        print('严重肥胖')
    else:
        print('非常严重的肥胖')

    print('香港医院管理局（HKHA）：', end='')
    if bmi < 18.5:
        print('体重不足')
    elif bmi < 23:
        print('正常范围')
    elif bmi < 25:
        print('超重，面临风险')
    elif bmi < 30:
        print('超重，重度肥胖')
    else:
        print('严重肥胖')

    print('日本肥胖研究学会（JASSO）：', end='')
    if bmi < 18.5:
        print('低体重')
    elif bmi < 25:
        print('正常体重')
    elif bmi < 30:
        print('一级肥胖')
    elif bmi < 35:
        print('二级肥胖')
    elif bmi < 40:
        print('三级肥胖')
    else:
        print('四级肥胖')

    print('新加坡：', end='')
    if bmi < 18.5:
        print('有营养缺乏、骨质疏松等风险')
    elif bmi < 23:
        print('低风险，健康范围')
    elif bmi < 27.5:
        print('中等风险罹患心脏病、高血压、中风和糖尿病')
    else:
        print('高风险罹患心脏病、高血压、中风和糖尿病')


if __name__ == '__main__':
    main()
