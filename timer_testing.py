#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 不能直接import function
#from threading import Timer, currntThread
import threading
import time
def delayrun():
    print "current thread is %s" % threading.currentThread().getName()
    
if __name__ == "__main__": 
    interval = 1
    #Timer是一个一次性的行为，即只执行一次，并且在另一个线程中执行
    t = threading.Timer(interval, delayrun)
    t.start()
    while True:
        time.sleep(0.1)
        print "This is main thread, name is %s" % threading.currentThread().getName()
