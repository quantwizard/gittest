#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from lxml import etree
from httplib2 import Http
import json
import re
 
 
class JdPrice(object):
    """
    对获取京东商品价格进行简单封装
    """
    def __init__(self, url):
        self.url = url
        self.http = Http()
        self._response, self.html = self.http.request(self.url)
 
    def get_product(self):
        """
        获取html中，商品的描述(未对数据进行详细处理，粗略的返回str类型)
        :return:
        """
        product_re = re.compile(r'compatible: true,(.*?)};', re.S)
        product_info = re.findall(product_re, self.html)[0]
        return product_info
 
    def get_product_skuid(self):
        """
        通过获取的商品信息，获取商品的skuid
        :return:
        """
        product_info = self.get_product()
        #print product_info
        skuid_re = re.compile(r'skuid: (.*?),')
        skuid = re.findall(skuid_re, product_info)[0]
        return skuid
 
    def get_product_name(self):
        pass
 
    def get_product_price(self):
        """
        根据商品的skuid信息，请求获得商品price
        :return:
        """
        price = None
        skuid = self.get_product_skuid()
        url = 'http://p.3.cn/prices/mgets?skuIds=J_' + skuid + '&type=1'
        resp, data = self.http.request(url)
        price_json = json.loads(data)[0]
        if price_json['p']:
            price = price_json['p']
        return price
 
 
# 测试代码
if __name__ == '__main__':
    
    itemUrl = "http://item.jd.com/132647.html"
    
    jp = JdPrice(itemUrl)
    print jp.get_product_price()
