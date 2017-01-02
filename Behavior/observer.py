#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Subscriber(object):

    def __init__(self, name):
        self._name = name

    def update(self, obj):
        print '{} updated: "{}"'.format(self._name, obj)


class NewsFeed(object):

    def __init__(self):
        self._subcriber = []

    def add_subscribe(self, scb):
        self._subcriber.append(scb)

    def remove_subscribe(self, scb):
        self._subcriber.remove(self._subcriber.index(scb))

    def notify(self, news):
        for sub in self._subcriber:
            sub.update(news)


def observer_use_case():
    feeder = NewsFeed()
    s1 = Subscriber('s1')
    s2 = Subscriber('s2')

    feeder.add_subscribe(s1)
    feeder.add_subscribe(s2)

    feeder.notify('First News')


if __name__ == '__main__':
    observer_use_case()

