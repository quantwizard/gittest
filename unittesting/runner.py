#!/usr/bin/env python  
#encoding: utf-8  
  
import unittest  
import myclass, mytest
import mytest2

suit = unittest.TestLoader().loadTestsFromModule(mytest)
suit.addTests(unittest.TestLoader().loadTestsFromModule(mytest2))
unittest.TextTestRunner(verbosity=2).run(suit)
