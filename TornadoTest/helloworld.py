#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.ioloop as loop
import tornado.web as web

class MainHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, tornado!")

def make_app():
    return web.Application([
        (r'/', MainHandler),
    ])

def main():
    app = make_app()
    app.listen('8899')
    loop.IOLoop.current().start()

if __name__ == '__main__':
    main()
