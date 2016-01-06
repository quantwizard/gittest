#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from time import sleep


def main():
    cur_pid = os.getpid()
    print "current pid is:", cur_pid
    pid = os.fork()
    print "child pid is:", pid

    if pid > 0:
        sleep(5)
        print "-current pid is:", os.getpid()
        sys.exit(0)
        # print "-current pid is:", os.getpid()

    for i in range(10):
        print i
        print "current pid is:", os.getpid()
        sleep(5)

if __name__ == '__main__':
    main()