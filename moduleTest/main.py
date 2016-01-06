#!/usr/bin/env python
#from moduleLib.moduletest import *
from moduleLib import moduletest

a = 0
b = 'xxx'

def foo():
    '''
    this is foo function.
    '''
    print "in foo function"


def main():
    '''
    this is main function
    '''
    print __builtins__
    print "doc in main %s" % __doc__
    print "name in main %s" % __name__
    print "file in main %s" % __file__
    print __package__
    print "mo_var2 in main %s" % moduletest.mo_var2

if __name__ == '__main__':
    main()
