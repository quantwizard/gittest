#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Flask, redirect
from werkzeug import secure_filename
from flask import url_for
from flask import request
app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        file_name = secure_filename(f.filename)
        f.save(os.path.join('/Users/eliu/code/gittest/flask/uploads/', file_name))
        return redirect(url_for('upload_file'))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=the_file>
         <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__':
    app.run(debug=True)
