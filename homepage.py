from flask import Flask
from flask import render_template
from flask import request
import requests

@app.route('/', methods=['GET', 'POST']
def root():
    if request.method == 'POST':
        return render_template('post.html');
    return render_template('get.html');
