#!/usr/bin/env python
# -*- coding: utf-8 -*-

from httplib2 import Http
from lxml import etree
from StringIO import StringIO
from time import sleep
from subprocess import Popen
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
password_ori = ""


def getPage():
    """
    get html page
    """
    url = "http://www.ishadowsocks.com/"
    http = Http()
    resp, content = http.request(url)
    # print resp
    return content


def getPassword(htmlPage):
    """
    Parse the html page and get the password
    """
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(htmlPage), parser)
    xPath = "//section[@id='free']/div[1]/div[2]/div[1]/h4[3]"
    passwordNode = tree.xpath(xPath)
    # print passwordNode[0].text
    return passwordNode[0].text.split(":")[-1]

def main():
    
    while(True):
    # for i in range(10):
        page = getPage()
        password = getPassword(page)
        global password_ori
        if password != password_ori:
            password_ori = password
            cmd = "say 'password changed'"
            Popen(cmd, shell=True)
            print password_ori
        sleep(10)

if __name__ == '__main__':
    main()