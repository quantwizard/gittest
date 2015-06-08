#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


url1 = 'http://www.baidu.com/s'
url2 = 'http://github.com/timeline.json'
payload = {'wd':'编程', 'rn':'100'}
re = requests.get(url2)
print re.url
print re.status_code
print re.content
