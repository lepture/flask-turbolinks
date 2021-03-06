from flask import Flask, redirect, request
from flask_turbolinks import turbolinks


app = Flask(__name__)
app.secret_key = 'secret'

turbolinks(app)


@app.route('/')
def home():
    return request.referrer or ''


@app.route('/page')
def page():
    return 'page'


@app.route('/redirect')
def in_redirect():
    return redirect('/page')


@app.route('/x-redirect')
def x_redirect():
    return redirect('http://lepture.com')


def test_home():
    client = app.test_client()
    rv = client.get('/', headers={
        'X-XHR-Referer': '/page'
    })
    assert '/page' == rv.data.decode('utf-8')
    assert 'request_method=GET' in rv.headers['Set-Cookie']


def test_redirect():
    client = app.test_client()
    rv = client.get('/redirect', headers={
        'X-XHR-Referer': '/page'
    })
    assert 'X-XHR-Redirected-To' not in rv.headers


def test_cookie():
    client = app.test_client()
    rv = client.get('/', headers={
        'Cookie': 'request_method=GET'
    })
    assert 'Set-Cookie' not in rv.headers


def test_x_redirect():
    client = app.test_client()
    rv = client.get('/x-redirect')
    assert rv.status_code == 302

    rv = client.get('/x-redirect', headers={
        'X-XHR-Referer': '/page'
    })
    assert rv.status_code == 200
    assert b'script' in rv.data

    rv = client.get('/x-redirect', headers={
        'X-XHR-Referer': 'http://example.com/'
    })
    assert rv.status_code == 200
    assert b'script' in rv.data

    rv = client.get('/x-redirect', headers={
        'X-XHR-Referer': 'http://lepture.com:8000/'
    })
    assert rv.status_code == 200
    assert b'script' in rv.data

    rv = client.get('/x-redirect', headers={
        'X-XHR-Referer': 'http://lepture.com/life/'
    })
    assert rv.status_code == 302
