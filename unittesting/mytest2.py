#!/usr/bin/env python  
#encoding: utf-8  
  
import unittest  
import myclass, mytest  
  
class mytest2(unittest.TestCase):  
      
    ##初始化工作  
    def setUp(self):  
        print "Setup in mytest2......"  
      
    #退出清理工作,不论最后assert的结果如何，都会执行tearDown，而且每个test method结束后都会执行 
    def tearDown(self):  
        print "Teardown....."  
      

    def testsum2(self):
        self.assertEqual(1, 2, 'in test2')

          
          
if __name__ =='__main__':  
    pass
