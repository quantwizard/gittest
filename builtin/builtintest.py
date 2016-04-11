#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TestVar(object):
    var1 = 1
    def __init__(self):
        self.var2 =2

    def testmethod(self):
        print "this is testmethod"

    def testmethod2(self):
        self.var3 = 3

def main():
    tester = TestVar()
    # tester.testmethod2()
    print "----vars----"
    print vars(tester)
    print "----dir----"
    print dir(tester)
    print "----help----"
    print help(tester)
    print "----hasattr---"
    print hasattr(tester, "var2")
    print hasattr(tester, "var3")

if __name__ == '__main__':
    main()