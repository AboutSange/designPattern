#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
1.2.做一个商场收银软件，营业员根据客户所购买商品的单价和数量，向客户收费
简单工厂模式
"""
import sys


def exit_with_info(info):
    """

    :param info:
    :return:
    """
    print(info)
    sys.exit(-1)


class CashFactory(object):
    """现金收费工厂类"""
    @staticmethod
    def create_cash_accept(type):
        cs = None
        if type == '正常收费':
            cs = CashNormal()
        elif type == '打8折':
            cs = CashRebate(0.8)
        elif type == '满300返100':
            cs = CashReturn(300, 100)
        else:
            exit_with_info('[error]请输入正确的收费类型')

        return cs


class CashSuper(object):
    """现金收费抽象类"""
    def accept_cash(self, money):
        return money


class CashNormal(CashSuper):
    """正常收费子类"""
    pass


class CashRebate(CashSuper):
    """打折收费子类"""
    def __init__(self, money_rebate):
        """

        :param money_rebate: 折扣率
        """
        self.money_rebate = money_rebate

    def accept_cash(self, money):
        return money * self.money_rebate


class CashReturn(CashSuper):
    """返利收费子类"""
    def __init__(self, money_condition, money_return):
        """

        :param money_condition: 满足条件
        :param money_return: 返利值
        """
        self.money_condition = money_condition
        self.money_return = money_return

    def accept_cash(self, money):
        if money >= self.money_condition:
            result = money - self.money_return
        else:
            result = money
        return result


def main():
    cs = CashFactory.create_cash_accept('满300返100')
    total_prices = 300
    result = cs.accept_cash(total_prices)
    print(result)


if __name__ == '__main__':
    main()
