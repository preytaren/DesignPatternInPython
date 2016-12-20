# -*- encoding=utf-8 -*-
"""
bridge 模式
用于将接口与实现分离，分别放在两个平行的类层次中
"""


class Pet(object):

    def __init__(self, food):
        self.food = food

    def eat(self):
        pass


class Cat(Pet):

    def eat(self):
        print 'Cat eat'
        print self.food.eaten()


class Dog(Pet):

    def eat(self):
        print 'Dog eat ' + self.food.get_name()


class Food(object):
    def get_name(self):
        raise NotImplementedError


class Fish(Food):
    def get_name(self):
        return 'fish'


class Burger(Food):

    def get_name(self):
        return 'burger'


if __name__ == '__main__':
   fish = Fish()
   burger = Burger()

   cat = Cat(fish)
   dog = Dog(burger)

   cat.eat()
   dog.eat()
