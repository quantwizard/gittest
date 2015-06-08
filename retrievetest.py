#! /usr/bin/env python 
# coding: utf-8 
"""下载文件，并显示下载进度"""
import urllib
 
def DownCall(count,size,total_filesize):
    """count为已下载数据块个数，size为数据块的大小，total_filesize为文件总大小"""
    '''print "count is : %s" % count
    print "size is: %s" % size
    print "total file size is: %s" % total_filesize
    '''

    per=100.0*count*size/total_filesize
    if per>100:
        per=100
    print "Already download %d KB(%.2f"  %(count*size/1024,per)+"%)"
 
url="http://www.163.com"
localfilepath=r"C:\Users\Eric\Desktop\download163.html"
urllib.urlretrieve(url,localfilepath,DownCall)
