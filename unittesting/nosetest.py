#!/usr/bin/env python
# -*- coding: utf-8 -*-


from nose.plugins.attrib import attr
import unittest



class TestClass1(unittest.TestCase):
    '''this is testclass1'''
    def setup(self):
        print "this is TestClass1 setup method."

    def teardown(self):
        print "this is TestClass1 teardown method."

    @attr('tag1')
    def test01(self):
        print "test01"
        assert True

    def test02(self):
        print "test02"
        assert False


class TestClass2(unittest.TestCase):
    '''this is testclass2'''
    def setup(self):
        print "this is TestClass2 setup method."

    def teardown(self):
        print "this is TestClass2 teardown method."

    @attr('tag1')
    def test03(self):
        '''this is test03'''
        print "test03"
        assert True

    def test04(self):
        print "test04"
        assert False