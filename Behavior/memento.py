#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Memento 模式
常用于需要对对象状态进行存储，以支持后续恢复操作的场景，
通过一个备忘录对象，避免了对象内部状态的暴露
"""
# todo 增量式
import zlib
from collections import deque


class Document(object):

    def __init__(self):
        self._lines = []
        # 支持最多十次撤销
        self._memo_list = deque(maxlen=10)

    def add_line(self, line, indent=0):
        actual_line = ' ' * indent + line
        self._lines.append(actual_line)
        self._memo_list.append(DocumentMemo(self))

    def add_lines(self, lines, indent=0):
        actual_lines = [' ' * indent + line for line in lines]
        self._lines.extend(actual_lines)
        self._memo_list.append(DocumentMemo(self))

    def undo_add(self):
        if len(self._memo_list) == 1:
            memo = self._memo_list.pop()
            del self._lines[0:]
        elif len(self._memo_list) > 1:
            _ = self._memo_list.pop()
            memo = self._memo_list[-1]
            memo._restore(self)

    @property
    def memo(self):
        if len(self._memo_list) > 0:
            return self._memo_list[-1]
        else:
            return DocumentMemo(self)

    @memo.setter
    def memo(self, memo):
        memo._restore(self)
        self._memo_list.append(memo)

    def __str__(self):
        return '\n'.join(self._lines)


class DocumentMemo(object):

    def __init__(self, doc_obj):
        docs = '|'.join(doc_obj._lines)
        self._compressed_doc = zlib.compress(docs)

    def _restore(self, doc_obj):
        doc_obj._lines = zlib.decompress(self._compressed_doc).split('|')


def memo_use_case():
    doc = Document()
    doc.add_line('Contents:')
    doc.add_line('This is the 1st line', indent=4)
    doc.add_line('This is the 2st line', indent=4)
    memo = doc.memo

    print 'Original Document:'
    print doc

    doc.undo_add()

    print 'After Undo:'
    print doc

    doc.memo = memo
    print 'After Restore:'
    print doc


if __name__ == '__main__':
    memo_use_case()