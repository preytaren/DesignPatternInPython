# -*- encoding=utf-8 -*-
"""
Composite 模式
主要用于处理类层次的递归组合，忽略组合对象和单个对象之间的差别
"""


class Block(object):

    def __init__(self):
        self._blocks = []

    def create(self):
        print 'create an block'
        for block in self._blocks:
            block.create()

    def add_block(self, block):
        self._blocks.append(block)

    def remove_block(self, block):
        self._blocks.remove(block)


class Entity(object):

    def __init__(self, name):
        self.name = name

    def create(self):
        print 'create an entity %s' % self.name


if __name__ == '__main__':
    block = Block()
    child_block = Block()
    block.add_block(child_block)

    child_block.add_block(Entity('foo'))
    child_block.add_block(Entity('bar'))

    block.create()
