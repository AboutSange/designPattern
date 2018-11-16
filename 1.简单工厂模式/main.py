#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
1.实现一个计算器控制台应用程序，要求输入两个数，和运算符号，得到结果
"""
import sys


def calculator(a, b, symbol):
    """

    :param a:
    :param b:
    :param str symbol: 运算符号
    :return: The result
    """
    if symbol == '+':
        return float(a) + float(b)
    elif symbol == '-':
        return float(a) - float(b)
    elif symbol == '*':
        return float(a) * float(b)
    elif symbol == '/':
        return float(a) / float(b)
    else:
        print('请输入正确的运算符号')
        sys.exit(-1)


def main():
    result = calculator(1, 0, '/')
    print(result)

if __name__ == '__main__':
    main()
