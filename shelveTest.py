#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shelve
"""
shelve is a db like stuff which can store persistant data
"""

def main():
    d = shelve.open("shelvedb.db")
    # data = {"a": 1, "b": 2, "c": 3}
    # d["dict"] = data
    print d["dict"]

    if d.has_key("xxx"):
        print d["xxx"]
    else:
        d["xxx"] = 8

    print d.keys()
    d.close()

if __name__ == '__main__':
    main()