# -*- encoding=utf-8 -*-
"""
FlyWeight 模式
用于处理大量重复的类的共享
"""


class DigitFactory(object):

    def __init__(self):
        self._digits = {}

    def get_digit(self, key):
        if key not in self._digits:
            self._digits[key] = Digit(key)
        return self._digits[key]


class Digit(object):

    def __init__(self, name):
        self.name = name


class NewDigit(object):

    _digits = {}

    def __new__(cls, key):
        if key not in cls._digits:
            cls._digits[key] = super(NewDigit, cls).__new__(cls, key)
        return cls._digits[key]

    def __init__(self, key):
        self._key = key


if __name__ == '__main__':
    factory = DigitFactory()

    a1 = factory.get_digit('A')
    a2 = factory.get_digit('A')

    b = factory.get_digit('B')

    assert id(a1) == id(a2)
    assert id(a1) != id(b)

    a3 = NewDigit('a')
    a4 = NewDigit('a')

    assert id(a3) == id(a4)
