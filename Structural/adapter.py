# -*- encoding=utf-8 -*-
"""
Adapter 模式
适配器模式主要用于处理现有类和框架接口不兼容的情况
下面描述了一个汽车适配器的简单例子
"""


class TargetCar(object):

    def run(self):
        print 'Car is running'

    def stop(self):
        print 'Car is stopped'


class RealCar(object):

    def move(self):
        print 'Car is moving'

    def stop(self):
        print 'Car is stopped'


class CarAdapter(object):

    def __init__(self):
        self._car = RealCar()

    def run(self):
        # do something else here
        self._car.move()

    def stop(self):
        # do something else here
        self._car.stop()


def test_a_car(car):
    car.run()
    car.stop()


if __name__ == '__main__':
   car = CarAdapter()
   test_a_car(car)
