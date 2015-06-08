#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
from httplib2 import Http
from HTMLParser import HTMLParser
import time
import StringIO
import urlparse
import re

class BuildReportHtmlParser(HTMLParser):
    infoFlag = 0
    InfoList = []
     
    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.infoFlag = 1
         
    def handle_endtag(self, tag):
         if tag == "tr":
            self.infoFlag = 0
    
    def handle_data(self, data):                
        if self.infoFlag == 1:
            if len(data)>3:
                self.InfoList.append(data.strip())
                
    def getBranchName(self):
        index = self.InfoList.index("Branch:")
        return self.InfoList[index+1]
    
    def getBuildTag(self):
        try:
            index = self.InfoList.index("Tag:")
            return self.InfoList[index+1]
        except Exception, ex:
            return ""
    
def getBuildTagWithLxml(htmlContent):
    build_page_parser = etree.HTMLParser()
    build_page_tree = etree.parse(StringIO.StringIO(htmlContent), build_page_parser)
    h1_elem_iter = build_page_tree.iter("h1")
    for e in h1_elem_iter:
        build_tag = e.text.split()[-1]
        return build_tag
    return ""

def parseWithRe():
    pass

def getBuildTagWithHtmlParser(htmlContent):
    parser = BuildReportHtmlParser()
    parser.feed(htmlContent)
    return parser.getBuildTag()

        
def getBuildReportHtml(buildId):
    buildURL = "http://mag-build.prognet.com/~build/report.cgi?id=" + buildId
    http = Http()
    resp, content = http.request(buildURL)
    return content  
    
def main():
    buildId = "30514"
    htmlContent = getBuildReportHtml(buildId)
    startTime = time.time()
    buildTag = getBuildTagWithHtmlParser(htmlContent)
    print buildTag
    endTime = time.time()
    print "getBuildTagWithHtmlParser use time: %s " % str(endTime - startTime)
    
    startTime = time.time()
    buildTag = getBuildTagWithLxml(htmlContent)
    print buildTag
    endTime = time.time()
    print "getBuildTagWithHtmlLxml use time: %s " % str(endTime - startTime)
    
if __name__ == "__main__":
    main()
