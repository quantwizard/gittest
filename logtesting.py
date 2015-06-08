#!/usr/bin/env python  
#encoding: utf-8

import sys
import inspect

def log(str):
    who = inspect.getframeinfo(inspect.currentframe().f_back)[2]
    print "[%s]: %s" % (who, str)

def testlog():
    log("in testlog")

if __name__=="__main__":
    testlog()
    
