#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Command 模式
通过将请求封装为一个对象，解耦请求发送者和接受者，
这种方式可以对请求排队，日志等功能进行支持，同时，
由于请求作为一个独立的对象，支持undo和redo操作
"""


class Document(object):

    def __init__(self, filename):
        self._contents = []
        self._filename = filename

    @staticmethod
    def open(filename):
        print 'Open file {}'.format(filename)
        return Document(filename)

    def add(self, message):
        print 'Add message : {}'.format(message)
        self._contents.append(message)

    def save(self):
        print "Save file '{0}': {1}...".format(self._filename, self._contents[:1])


class CommandMixin(object):

    def execute(self):
        raise NotImplementedError


class OpenCommand(CommandMixin):

    def __init__(self, filename):
        self._filename = filename

    def execute(self):
        return Document.open(self._filename)


class SaveCommand(CommandMixin):

    def __init__(self, document):
        self._document = document

    def execute(self):
        self._document.save()


class AddCommand(CommandMixin):

    def __init__(self, document, message):
        self._document = document
        self._message = message

    def execute(self):
        self._document.add(self._message)


class CommandHandler(object):

    def __init__(self):
        self._commands = []

    def add_command(self, command):
        self._commands.append(command)

    def flush(self):
        # 这里可以加入队列功能
        for command in self._commands:
            command.execute()


def non_command_use_case():
    # 打开文档
    document = Document.open('demo.txt')

    # 写入文档
    document.add('This is the first line')

    # 保存文档
    document.save()


def command_user_case():
    handler = CommandHandler()

    # 打开文档
    document = OpenCommand('demo.txt').execute()

    handler.add_command(AddCommand(document, 'This is the first line'))
    handler.add_command(SaveCommand(document))

    handler.flush()


if __name__ == '__main__':
    non_command_use_case()

    command_user_case()

