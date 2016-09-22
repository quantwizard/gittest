#!/usr/bin/env python
# -*- coding: utf-8 -*-


class DictTest(object):
    c_mode = None

    def __init__(self):
        self.o_var = None

    def foo(self):
        return True


def main():
    o = DictTest()
    print o.__dict__
    print type(o).__dict__


if __name__ == "__main__":
    main()