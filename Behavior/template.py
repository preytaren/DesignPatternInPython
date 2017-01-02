#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Template 模式
通过将相同的逻辑提取到基类，利用多态性质，
在不同子类中实现不同的功能
"""


class BaseClass(object):

    def compete(self):
        print 'Competetion Start:'
        self.run()
        self.jump()
        print 'Competetion End!'

    def run(self):
        print 'BaseClass Run'

    def jump(self):
        print 'BaseClass Jump'


class Jeff(BaseClass):

    def run(self):
        print 'Jeff Run'

    def jump(self):
        print 'Jeff Jump'


def template_use_case():
    base = BaseClass()
    base.compete()

    jeff = Jeff()
    jeff.compete()


if __name__ == '__main__':
    template_use_case()
