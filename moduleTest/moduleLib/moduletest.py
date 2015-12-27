#!/usr/bin/env python

"""
this is module doc
"""

# __all__ = ['mo_var', '__module_hide']
mo_var = 3
mo_var2 = __name__
print mo_var2

def module_foo():
    '''
    this is module_foo doc
    '''
    print "in module_foo"


def __module_hide():
    '''
    this is __module_hide
    '''
    print "in __module_hide"


def _module_private():
    print "in _module_private"


if __name__ == '__main__':
    print __doc__