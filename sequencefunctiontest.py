#!/usr/bin/env python

def add(a, b):
    return a + b

if __name__ == '__main__':
    numbers = [1, 2, 3, 4]
    print map(lambda x: add(1, x), numbers)