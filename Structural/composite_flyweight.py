# -*- encoding=utf-8 -*-
"""
展示了一个
"""


class Item(object):
    pass


class Row(Item):

    def __init__(self, string):
        self._letters = []
        for letter in string:
            self._letters.append(Letter(letter))

    def draw(self, font_letter=''):
        return ''.join((letter.draw(font_letter) for letter in self._letters))


class Letter(Item):
    _letters = {}

    def __new__(cls, letter):
        if letter not in cls._letters:
            cls._letters[letter] = super(Letter, cls).__new__(cls, letter)
        return cls._letters[letter]

    def __init__(self, letter):
        self._letter = letter

    def draw(self, font_letter=''):
        return font_letter + self._letter


if __name__ == '__main__':
    row = Row('we are the champions')
    print row.draw()
    print row.draw('#')
