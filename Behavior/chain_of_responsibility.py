# -*- encoding=utf-8 -*-
"""
Chain of Responsibility
实际上职责链模式是将对不同情况对处理分拆到各个对象当中，
链式的处理，达到解耦的效果
"""


class Handler(object):

    def __init__(self, successor):
        self._successor = successor

    def handle(self, obj):
        raise NotImplementedError


class HandlerA(Handler):

    def handle(self, obj):
        if hasattr(obj, 'A'):
            print 'Handled by A'
        else:
            self._successor.handle(obj)


class HandlerB(Handler):

    def handle(self, obj):
        if hasattr(obj, 'B'):
            print 'Handled by B'
        else:
            self._successor.handle(object)


class HandlerBase(Handler):

    def handle(self, obj):
        print 'Handled by Base Handler'


class foo(object):
    pass


if __name__ ==  '__main__':
    handler_base = HandlerBase(None)
    handler_b = HandlerB(handler_base)
    handler_a = HandlerA(handler_b)

    bar = foo()
    handler_a.handle(bar)

    bar.A = 'A'
    handler_a.handle(bar)


