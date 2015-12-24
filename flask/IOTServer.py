#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, abort
from flask import url_for, make_response, render_template
app = Flask(__name__)


@app.route('/', methods = ['POST'])
def handler():
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data
    elif request.headers['Content-Type'] == 'application/octet-stream':
        with open('./binary', 'wb') as f:
            f.write(request.data)
        return "Binary message got, check file binary"
    else:
        abort(400)


if __name__ == '__main__':
    app.run(debug=True)
