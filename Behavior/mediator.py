#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Mediator 模式
适用于多个对象相互依赖的场景，通过一个中介对象，使得各对象间不存在显式的引用
下面的例子展示了一个灯和两个按钮，它们都有开和关两个状态，按下按钮A会翻转另
按钮B和灯的状态，按下按钮B只会转换灯的状态
"""


class Button(object):

    def __init__(self, director, is_on=False):
        self._director = director
        self.is_on = is_on

    def click(self):
        self._director.click(self)

    def flip(self):
        if self.is_on:
            self.is_on = False
            print 'Turn off {}'.format(self.__class__.__name__)
        else:
            self.is_on = True
            print 'Turn on {}'.format(self.__class__.__name__)


class ButtonA(Button):
    pass


class ButtonB(Button):
    pass


class Light(object):

    def __init__(self):
        self.is_on = False

    def flip(self):
        if self.is_on:
            self.is_on = False
            print 'Turn off {}'.format(self.__class__.__name__)
        else:
            self.is_on = True
            print 'Turn on {}'.format(self.__class__.__name__)


class ButtonMediator(object):

    def __init__(self):
        self._button_a = None
        self._button_b = None
        self._light = None

    def set_button_a(self, button):
        self._button_a = button

    def set_button_b(self, button):
        self._button_b = button

    def set_light(self, light):
        self._light = light

    def click(self, item):
        if item == self._button_a:
           self._button_a.flip()
           self._button_b.flip()
           self._light.flip()
        elif item == self._button_b:
           self._button_b.flip()
           self._light.flip()
        else:
            raise KeyError('Unknown item {}'.format(item))


def non_mediator_use_case():

    class Button(object):
        def __init__(self):
            self.is_on = False
            self._another_button = None
            self._light = None

        def set_another_button(self, button):
            self._another_button = button

        def set_light(self, light):
            self._light = light

        def click(self):
            pass

        def flip(self):
            if self.is_on:
                self.is_on = False
                print 'Turn off {}'.format(self.__class__.__name__)
            else:
                self.is_on = True
                print 'Turn on {}'.format(self.__class__.__name__)

    class ButtonA(Button):

        def click(self):
            self.flip()
            self._another_button.flip()
            self._light.flip()

    class ButtonB(Button):

        def click(self):
            self.flip()
            self._light.flip()

    # demo code
    button_a = ButtonA()
    button_b = ButtonB()
    light = Light()

    button_a.set_another_button(button_b)
    button_a.set_light(light)
    button_b.set_another_button(button_a)
    button_b.set_light(light)

    print 'Click Button A:\n'
    button_a.click()
    print ''
    print 'Click Button B:'
    button_b.click()




def mediator_use_case():
    mediator = ButtonMediator()

    button_a = ButtonA(mediator)
    button_b = ButtonB(mediator)
    light = Light()

    mediator.set_button_a(button_a)
    mediator.set_button_b(button_b)
    mediator.set_light(light)

    print 'Click Button A:\n'
    button_a.click()
    print ''
    print 'Click Button B:'
    button_b.click()


if __name__ == '__main__':
    print 'Non mediator use case:'
    non_mediator_use_case()

    print 'Mediator use case:'
    mediator_use_case()
