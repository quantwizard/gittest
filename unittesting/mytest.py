#!/usr/bin/env python
# encoding: utf-8

import unittest
import myclass


class mytest(unittest.TestCase):

    # 初始化工作
    # 在nose中也是每个method都会执行setup teardown

    @classmethod
    def setup_class(self):
        print "class setup......"
        self.i = 1

    # 退出清理工作,不论最后assert的结果如何，都会执行tearDown，而且每个test method结束后都会执行
    @classmethod
    def teardown_class(self):
        print "class teardown....."

    def setup(self):
        print "setup...."

    def teardown(self):
        print "teardown..."

    # 具体的测试用例，一定要以test开头，然后说白了就是调用被测模块的函数来进行检测其结果是否符合预期
    def testsum(self):
        # self.assertEqual(myclass.sum(1, 2), 2, 'test sum fail')
        self.assertEqual(self.i, 1)
        self.i = 2

    def testsub(self):
        # self.assertEqual(myclass.sub(2, 1), 1, 'test sub fail')
        self.assertEqual(self.i, 1)
        self.i = 3

    def testrandom(self):
        # self.assertEqual(1, 1, 'must be true')
        self.assertEqual(self.i, 1)
        self.i = 4

    def testrandom2(self):
        self.assertEqual(1, 2, 'must be false')

    # 也可以用通用的assert来判断结果
    def testrandom3(self):
        assert len('hahahha') > 1, "it is false"


if __name__ == '__main__':
    unittest.main()
