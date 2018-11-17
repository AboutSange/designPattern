#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
1.实现一个计算器控制台应用程序，要求输入两个数，和运算符号，得到结果

version: 1.1.2
1.将无意义的变量名改掉
2.增加判断除数为0的情况
3.加入让用户输入的语句
4.将退出语句封装成exit_with_info方法

version: 1.1.3
1.使用面向对象思想，使程序可维护（要改，只需更改要改之字）、可扩展（若要加字，另刻字加入即可）、可复用（可重复使用）、灵活性好（能灵活满足各种需求）
    通过封装、继承、多态把程序的耦合性降低，
    用设计模式使程序更加灵活，容易修改，并且易于复用
2.将业务逻辑与界面逻辑分开来，使其耦合性下降

version: 1.1.4
1.简单工厂模式
2.UML：继承、实现、关联、依赖、聚合、合成
"""
import sys


def exit_with_info(info):
    """

    :param info:
    :return:
    """
    print(info)
    sys.exit(-1)


class OperationFactory(object):
    """简单工厂类"""
    @staticmethod
    def create_operate(operate):
        """

        :param operate:
        :return:
        """
        if operate == '+':
            oper = OperationAdd()
        elif operate == '-':
            oper = OperationSub()
        elif operate == '*':
            oper = OperationMul()
        elif operate == '/':
            oper = OperationDiv()
        else:
            exit_with_info('[error]请输入正确的运算符')
        return oper


class Operation(object):
    """运算类"""
    number_a = 0
    number_b = 0

    def get_result(self):
        result = 0
        return result


class OperationAdd(Operation):
    """加法类"""
    def get_result(self):
        number_a = float(self.number_a)
        number_b = float(self.number_b)

        result = number_a + number_b
        return result


class OperationSub(Operation):
    """减法类"""
    def get_result(self):
        number_a = float(self.number_a)
        number_b = float(self.number_b)

        result = number_a - number_b
        return result


class OperationMul(Operation):
    """乘法类"""
    def get_result(self):
        number_a = float(self.number_a)
        number_b = float(self.number_b)

        result = number_a * number_b
        return result


class OperationDiv(Operation):
    """除法类"""
    def get_result(self):
        number_a = float(self.number_a)
        number_b = float(self.number_b)
        if number_b == 0:
            exit_with_info('[error]除数不能为0')

        result = number_a / number_b
        return result


def main():
    oper = OperationFactory.create_operate('/')
    oper.number_a = 20
    oper.number_b = 0
    result = oper.get_result()
    print(result)


if __name__ == '__main__':
    main()
