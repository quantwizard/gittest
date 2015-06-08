
import urllib2
import urllib
import cookielib

'''cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('http://www.baidu.com')
for item in cookie:
    if item.name == 'BD_HOME':
        print item.value
'''
'''try:
    
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
    opener = urllib2.build_opener(httpHandler, httpsHandler)

    urllib2.install_opener(opener)
    response = urllib2.urlopen('http://www.google.com')

except urllib2.HTTPError, e:
    print e.code
'''
data1='lalalla'
data2 =  urllib.urlencode({'a':'jack', 'b':'bob'})

headers = {"Accept": "*/*",
               "Cache-Control": "no-cache",
               "Connection": "Keep-Alive",
               "User-Agent":"Mozilla/5.0"
               }
req = urllib2.Request('http://www.163.com/', headers=headers)
response = urllib2.urlopen(req,timeout=5)
print response.info()


