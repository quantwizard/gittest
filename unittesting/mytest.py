#!/usr/bin/env python  
#encoding: utf-8  
  
import unittest  
import myclass  
  
class mytest(unittest.TestCase):  
      
    ##初始化工作  
    def setUp(self):  
        print "Setup......"  
      
    #退出清理工作,不论最后assert的结果如何，都会执行tearDown，而且每个test method结束后都会执行 
    def tearDown(self):  
        print "Teardown....."  
      
    #具体的测试用例，一定要以test开头，然后说白了就是调用被测模块的函数来进行检测其结果是否符合预期  
    def testsum(self):  
        self.assertEqual(myclass.sum(1, 2), 2, 'test sum fail')  
          
          
    def testsub(self):  
        self.assertEqual(myclass.sub(2, 1), 1, 'test sub fail')

    def testrandom(self):
        self.assertEqual(1, 1, 'must be true')

    def testrandom2(self):
        self.assertEqual(1, 2, 'must be false')

    #也可以用通用的assert来判断结果
    def testrandom3(self):
        assert len('hahahha')>1, "it is false"
          
          
if __name__ =='__main__':  
    unittest.main()  
