#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, abort
from flask import url_for, make_response, render_template
app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def handler():
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data
    elif request.headers['Content-Type'] == 'application/octet-stream':
        with open('./binary', 'wb') as f:
            f.write(request.data)
        return "Binary message got, check file binary"
    elif request.headers['Content-Type'] == 'application/json':
        print "received json: %s" % request.data
	return "OK"
    else:
       	print "received data: %s" % request.data
	return "OK" 


if __name__ == '__main__':
    app.run(debug=True)
