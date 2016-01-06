# -*- coding: utf-8 -*-

import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient
import functools


def task(func, url):
    return functools.partial(func, url)
    # functools.partial用于给函数传递部分参数，这里func是函数，url是参数


def callback(gen, response):
    try:
        gen.send(response)
    except StopIteration:
        pass


def sync(func):         # here func is fetch() generator
    def wrapper():
        gen = func()    # gen is fetch generator
        f = gen.next()  
        # f is task(AsyncHTTPClient().fetch, url), and that means
        # f is AsyncHTTPClient().fetch(url, ), and it is a partial function
        f(functools.partial(callback, gen))
        # here means AsyncHTTPClient().fetch(url, callback(fetch(),)) 
        # callback(fetch(),) is still a function, but partial function
        # anyway, the client fetch url firstly. when the response is got
        # the partial function is called f(response) --> callback(fetch(), response)
    return wrapper


@sync
def fetch():
    response = yield task(AsyncHTTPClient().fetch, 'http://www.163.com')
    print '1'
    print response
    print '2'


def main():
    fetch()
    print '3'
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()