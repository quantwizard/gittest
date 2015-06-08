import httplib
import httplib2
import lxml.html
import lxml.etree
import StringIO

mag_build_url = 'http://mag-build.prognet.com/~build/builddb.cgi?start_date=&end_date=&days_ago=5&build_type=&id=&tag=&branch=rt_mac&module=&profile=&user=&platform=osx&options='
h = httplib2.Http()
try:
    (resp, content) = h.request(mag_build_url)

except Exception, e:
    print e
builds_page_parser = lxml.etree.HTMLParser()
builds_page_tree = lxml.etree.parse(StringIO.StringIO(content), builds_page_parser)
a_elem_iter = builds_page_tree.iter("a")
for i in a_elem_iter:
   
    if "report.cgi" in lxml.etree.tostring(i):
        print i.text
