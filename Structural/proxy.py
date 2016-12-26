# -*- encoding=utf-8 -*-
"""
proxy 模式
一个常见的用法就是延迟实际的求值操作
"""


class Rectangle(object):

    def __init__(self, height, width):
        print 'Create a Rectangle'
        self._height = height
        self._width = width

    def draw(self):
        print 'A rectangle of size: {height}x{width} = {size}'.format(height=self._height,
                                                                      width=self._width,
                                                                      size=self._width*self._height)


class RectangleProxy(object):

    def __init__(self, height, width):
        print 'Create a Proxy'
        self.height = height
        self.width = width
        self._last_height = height
        self._last_width = width
        self._instance = None

    def draw(self):
        if not self._instance \
               or self._last_width != self.width \
               or self._last_height != self.height:
            self._instance = Rectangle(self.height, self.width)
            self._last_height = self.height
            self._last_width = self.width
        self._instance.draw()


if __name__ == '__main__':
    height, width = 10, 20
    rectangle = RectangleProxy(height, width)
    rectangle.draw()
    rectangle.width = 30
    rectangle.draw()