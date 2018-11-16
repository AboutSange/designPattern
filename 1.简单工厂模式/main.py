#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
1.实现一个计算器控制台应用程序，要求输入两个数，和运算符号，得到结果

version: 1.1.2
1.将无意义的变量名改掉
2.增加判断除数为0的情况
3.加入让用户输入的语句
4.将退出语句封装成exit_with_info方法
"""
import sys


def calculator(number_a, number_b, symbol):
    """

    :param number_a:
    :param number_b:
    :param str symbol: 运算符号
    :return: The result
    """
    number_a = float(number_a)
    number_b = float(number_b)

    if symbol == '+':
        return number_a + number_b
    elif symbol == '-':
        return number_a - number_b
    elif symbol == '*':
        return number_a * number_b
    elif symbol == '/':
        if number_b == 0:
            exit_with_info('除数不能为0')
        return number_a / number_b
    else:
        exit_with_info('请输入正确的运算符号')


def exit_with_info(info):
    """

    :param info:
    :return:
    """
    print(info)
    sys.exit(-1)


def main():
    number_a = input('请输入数字A：')
    number_b = input('请输入数字B：')
    symbol = input('请输入运算符：')
    result = calculator(number_a, number_b, symbol)
    print(result)


if __name__ == '__main__':
    main()
