from urlparse import urlparse

o = urlparse('http://www.2nsoft.cn:80/bbs/thread.php?fid=120')

print o
print o.port
print o.query
