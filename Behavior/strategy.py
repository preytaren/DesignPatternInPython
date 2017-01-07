#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Strategy 模式
Web 开发里面的模版应用就是一个Strategy模式的例子，通过将模版和Context分离来达到解耦和复用的目的
下面展示一个将一段文字排版的示例
"""
from textwrap import TextWrapper


fill_with_no_first_line_indent = TextWrapper().fill

fill_with_first_line_indent = TextWrapper(initial_indent='    ').fill

fill_with_less_width = TextWrapper(initial_indent='    ', width=40).fill


def strategy_use_case():
    text = 'It was the best of times, it was the worst of times,' \
           ' it was the age of wisdom, it was the age of foolishness' \
           ', it was the epoch of belief, it was the epoch of ' \
           'incredulity, it was the season of Light, it was the season' \
           ' of Darkness, it was the spring of hope, it was the winter ' \
           'of despair, we had everything before us, we had nothing ' \
           'before us, we were all going direct to heaven, we were all' \
           ' going direct the other way - in short, the period was so ' \
           'far like the present period, that some of its noisiest ' \
           'authorities insisted on its being received, for good or ' \
           'for evil, in the superlative degree of comparison only.'

    print 'Oringinal text:'
    print text, '\n'

    print 'Fill with no first line indent:'
    print fill_with_no_first_line_indent(text), '\n'

    print 'Fill with no first line indent:'
    print fill_with_first_line_indent(text), '\n'

    print 'Fill with no first line indent:'
    print fill_with_less_width(text), '\n'


if __name__ == '__main__':
    strategy_use_case()
