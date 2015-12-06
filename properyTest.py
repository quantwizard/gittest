#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ProperTest(object):
    def __init__(self):
        self.__status = 0

    @property
    def status(self):
        print "you get status"
        return self.__status

    @status.setter
    def status(self, value):
        print "you set status"
        self.__status = value

    @status.deleter
    def status(self):
        print "you delete status"
        del self.__status


def main():
    pt = ProperTest()
    pt.status = 5
    print pt.status
    del pt.status
    # print pt.status

if __name__ == '__main__':
    main()
