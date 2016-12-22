# -*- encoding=utf-8 -*-
"""
Decorator 模式
在python 中有装饰器这个语法糖
"""
from functools import wraps


def deco(fn):
    """
    不带参数的装饰器
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print 'Before execute %s ' % fn.__name__
        result = fn(*args, **kwargs)
        print 'After execute %s ' % fn.__name__
        return result
    return wrapper


def doc_deco(docs):
    """
    带参数的装饰器
    """
    def func(fn):
        fn.__doc__ = docs

        @wraps(fn)
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)
        return wrapper
    return func


class Deco:

    def __init__(self, fn):
        self._fn = fn

    def __call__(self, *args, **kwargs):
        print 'Before execute %s ' % self._fn.__name__
        result = self._fn(*args, **kwargs)
        print 'After execute %s ' % self._fn.__name__
        return result


@deco
def test_function(message):
    print message


@doc_deco('This is a test function')
def test_function2():
    print 'test function'

@Deco
def test_function3():
    print 'Hello '


if __name__ == '__main__':
    test_function('Hello world')
    assert test_function2.__doc__ == 'This is a test function'
    test_function3()
