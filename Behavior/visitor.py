#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""
Visitor 模式
适用于在一族对象上进行遍历的某种操作，
可以分离对象的结构和在对象上的操作,
在pytho中可以很好的使用生成器和生成
器表达式来完成这类工
"""
from collections import Iterator


class Node:

    def __init__(self, value):
        self._children = []
        self.value = value

    def apply(self, visitor):
        visitor.visit(self)
        for child in self._children:
            child.apply(visitor)

    def add_node(self, *nodes):
        for node in nodes:
            self._children.append(node)


class Leaf(Node):

    def __init__(self, value):
        super(Leaf, self).__init__(value)

    def apply(self, visitor):
        return visitor.visit(self)

    def add_node(self, node):
        raise NotImplementedError


class CountVisitor:

    def __init__(self):
        self.count = 0

    def visit(self, node):
        self.count += 1


class ValueCountVisitor:
    def __init__(self):
        from collections import Counter
        self.counter = Counter()

    def visit(self, node):
        self.counter[node.value] += 1


def visitor_use_case():
    root = Node('root')

    n1 = Node('n1')
    n2 = Node('n2')
    n3 = Node('n3')

    l1 = Leaf('l1')
    l2 = Leaf('l2')
    l3 = Leaf('l3')

    root.add_node(n1, n2, n3)
    n1.add_node(l1, l2)
    n2.add_node(l3)

    count_visitor = CountVisitor()
    root.apply(count_visitor)

    assert count_visitor.count == 7

    another_count_visitor = ValueCountVisitor()
    root.apply(another_count_visitor)
    print(another_count_visitor.counter)


# 生成器的方式
class IterNode:

    def __init__(self, value):
        self._children = []
        self.value = value

    def add_node(self, *nodes):
        self._children.extend(nodes)

    def __iter__(self):
        yield self
        for child in self._children:
            yield from child


class IterLeaf(IterNode):

    def __init__(self, value):
        super(IterLeaf, self).__init__(value)

    def add_node(self, *nodes):
        raise NotImplementedError

    def __iter__(self):
        yield self


def iter_use_case():
    root = IterNode('root')

    n1 = IterNode('n1')
    n2 = IterNode('n2')
    n3 = IterNode('n3')

    l1 = IterLeaf('l1')
    l2 = IterLeaf('l2')
    l3 = IterLeaf('l3')

    root.add_node(n1, n2, n3)
    n1.add_node(l1, l2)
    n2.add_node(l3)

    visitor = ValueCountVisitor()
    [visitor.visit(node) for node in root]

    print(visitor.counter)


if __name__ == '__main__':
    visitor_use_case()
    iter_use_case()