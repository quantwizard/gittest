#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cPickle import *


def main():
    test_obj1 = {"name": "Jack", "age": 22, "score": "B"}
    test_obj2 = {"name": "John", "age": 20, "score": "A"}

    # pickling to file
    obj_file = open("objFile.pic", "w")
    dump(test_obj1, obj_file, 2)
    dump(test_obj2, obj_file, 2)
    obj_file.close()

    # unpickling
    obj_file = open("objFile.pic", "r")
    try:
        while True:
            obj = load(obj_file)
            print obj
    except:
        pass


if __name__ == '__main__':
    main()
