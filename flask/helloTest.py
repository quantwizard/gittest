#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, abort
from flask import url_for, make_response, render_template
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    about_link = "<a href='" + url_for('about') + "'>About</a>"

    return """
            <html>
                <head>
                    <title>hello, world!</title>
                </head>
                <body>
                    <p>Hello, World!</p>
                    <p>""" + about_link +"""
                </body>
            </html>
    """

@app.route('/post/<int:post_id>/')
def post_id(post_id):
    return "this is post id test, id: %d" % post_id

@app.route('/projects/')
def projects():
    args_content = request.args.get('name')
    # print type(args_content)
    return 'The project page, and the args is %s' % args_content

@app.route('/about')
def about():
    return 'The about page'


@app.route('/abort/')
def abortres():
    abort(401)

@app.route('/json')
def jsonres():
    return json.dumps({"name": "John", "age": 22})


@app.route('/login/')
def login():
    print "in login"
    resp = make_response(render_template('login.html'))
    resp.set_cookie('username', 'hahaha')
    return resp


if __name__ == '__main__':
    app.run(debug=True)
