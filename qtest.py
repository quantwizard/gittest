#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Queue import Queue, Empty
from threading import Thread

class QTest:
    def __init__(self):
        self.__queue = Queue()

    def putData(self, data):
        self.__queue.put(data)

    def getData(self):
        return self.__queue.get(block = True, timeout =1)

if __name__ == "__main__":
    qt = QTest()
    print "put data"
    qt.putData("1111")
    print "get data"
    str = qt.getData()
    print "get a data: %s" % str
    
