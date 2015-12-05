#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script is used to understand staticmethod and classmethod
and cls of python, also understand __new__
"""


class AdvanceUsage(object):

    # if we use *args, **kwargs， we can pass any amount of arguments
    def __init__(self, *args, **kwargs):
        print "in AdvanceUsage init", args, kwargs


    # no *args, **kwgs is ok
    # def __new__(cls):
    #     print "in AdvanceUsage new", cls
    #     return object.__new__(cls)

    # __new__ is called when create object instance
    # __init__ is called after the object instance is created.
    def __new__(cls, *args, **kwargs):
        print "in AdvanceUsage new", cls, args, kwargs
        return object.__new__(cls, *args, **kwargs)

    # static method do not need 'self' parameter
    @staticmethod
    def foo1():
        print "in static method"

    # class method have parameter 'cls', cls is class itself
    @classmethod
    def foo2(cls):
        print "in classmethod, cls is", cls


class ChildUsage(AdvanceUsage):
    def __init__(self):
        print "in child init"

    def __new__(cls):
        print "in child new", cls.__name__
        return super(ChildUsage, cls).__new__(cls)


def main():
    au = AdvanceUsage()
    au2 = AdvanceUsage("aa", "bb", 123, name="John")
    au.foo1()
    au.foo2()
    AdvanceUsage.foo1()
    AdvanceUsage.foo2()
    cu = ChildUsage()


if __name__ == '__main__':
    main()
