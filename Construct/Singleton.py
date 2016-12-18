# -*- encoding=utf-8 -*-
"""
Singleton 模式
下面展示了Python中实现Singleton的两种方式，
分别是使用装饰器，使用元类的方式
"""


class Singleton(type):

    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__call__(*args)
        return cls._instance


def singleton_dec(cls):
    instances = {}

    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrap


class TestSingleton:

    __metaclass__ = Singleton


if __name__ == '__main__':
   r1 = TestSingleton()
   r2 = TestSingleton()
   assert id(r1) == id(r2)
