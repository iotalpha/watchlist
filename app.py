# -*- coding: utf-8 -*-
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/home')
def hello():
    # return u'欢迎来到我的 Watchlist!'
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % name


@app.route('/test')
def test_url_for():
    print(url_for('hello'))     # Generates a URL to the given endpoint with the method provided
    print(url_for('user_page', name="greyli"))
    print(url_for('user_page', name='peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))

    return 'Test page'
