#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time

def func1(word):
    time.sleep(5)
    print "func1's word is: %s\r\n" % word
    time.sleep(2)
    print "func1 is over\r\n"

def func2(word):
    time.sleep(5)
    print "func2's word is: %s\r\n" % word
    time.sleep(2)
    print "func2 is over\r\n"

threads = []
t1 = threading.Thread(target=func1, args=("hahahha",))
threads.append(t1)

t2 = threading.Thread(target=func2, args=("lalallala",))
threads.append(t2)

if __name__ == "__main__":
    for t in threads:
        t.setDaemon(True)
        t.start()
    print "laadfdfjd"
    '''join will block current thread(main thread here),
        wait until thread t is over or timeout'''
    t.join(30)
    print "main thread is over!"
