#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Person(object):
    def __init__(self, name=None):
        self.name = name

    def show(self):
        print('装扮的{}'.format(self.name))


class Finery(Person):
    component = None

    def decorate(self, component):
        self.component = component

    def show(self):
        if self.component is not None:
            self.component.show()


class Tshirt(Finery):
    def show(self):
        print('T恤', end=' ')
        super(Tshirt, self).show()


class Trouser(Finery):
    def show(self):
        print('垮裤', end=' ')
        super(Trouser, self).show()


class Shoe(Finery):
    def show(self):
        print('运动鞋', end=' ')
        super(Shoe, self).show()


class Tie(Finery):
    def show(self):
        print('领带', end=' ')
        super(Tie, self).show()


def main():
    p = Person("Newbee")
    tr = Trouser()
    ts = Tshirt()
    ti = Tie()
    sh = Shoe()

    tr.decorate(p)
    ts.decorate(tr)
    ti.decorate(ts)
    sh.decorate(ti)
    sh.show()


if __name__ == '__main__':
    main()
