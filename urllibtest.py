# -*- coding: utf-8 -*-
import urllib

param = urllib.urlencode({'q':'url+编码'})
url = 'http://cn.bing.com/search?%s' % param
print url
url2 = 'http://cn.bing.com/search?q=url+encode+编码'
print 'quote result'
print urllib.quote(url2)
obj = urllib.urlopen(url)
print 'http header:\n', obj.info()
print 'http status:', obj.getcode()
print 'url:', obj.geturl()
print 'readline:', obj.readline()

'''for line in obj.readlines():
    print line
print '-------------------------'
for li in obj:
    print li
'''
obj.close()
