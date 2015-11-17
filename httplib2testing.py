import httplib2
import urllib
import urlparse

'''name="notfatboy@126.com"
password="nihao123"
url = "http://www.douban.com"
h = httplib2.Http()
h.add_credentials(name, password)
resp, content = h.request(url)

print resp
print "------------------------"
print content
'''

'''Post something to website'''
'''body="test test"
url2="http://www.douban.com/note/create"
resp, content =h.request(url2, "PUT", body, headers={'content-type':'text/plain'})
'''
httplib2.debuglevel = 1
http = httplib2.Http(".cache")
url = "http://uliweb.clkg.org/login"
url2 = "http://mag-build.prognet.com/~build/builddb.cgi?start_date=&end_date=&days_ago=3&build_type=&id=&tag=&branch=jupiter&module=player_master&profile=&user=&platform=&options="
url3 = "http://www.diveintopython.net/"
url4 = "http://mag-build.prognet.com/~build/build/jupiter/player_master/player_master-150524-998"

version = url4.split("/")[-1]
print version

body = {'username': 'python', 'password': 'python', 'rememberme': "True"}
headers = {'Content-type': 'application/x-www-form-urlencoded',
           "Connection": "Keep-Alive",
           "cache-control": "no-cache",
           }
response, content = http.request(url2, 'GET', headers=headers,)
print "---------content----------------"
print response
print "--------------------------------"
print "Content Length is: %s" % response['content-length']


'''csrf_val = content.split('csrf_token" value="')[1].split('">')[0]
body['csrf_token'] = csrf_val
headers['Cookie']= response['set-cookie']
response,content = http.request(url,'POST',headers=headers,body=urllib.urlencode(body))
url='http://uliweb.clkg.org/forum'
response,content=http.request(url,'GET',headers=headers)
print content
'''
