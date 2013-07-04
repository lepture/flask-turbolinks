from flask import Flask, redirect, request
from flask_turbolinks import turbolinks


app = Flask(__name__)
app.secret_key = 'secret'

turbolinks(app)


@app.route('/')
def home():
    return request.referer or ''


@app.route('/page')
def page():
    return 'page'


@app.route('/redirect')
def in_redirect():
    return redirect('/page')


@app.route('/x-redirect')
def x_redirect():
    return redirect('http://lepture.com')


client = app.test_client()


def test_home():
    rv = client.get('/', headers={
        'X-XHR-Referer': '/page'
    })
    assert '/page' == rv.data
    assert 'request_method=GET' in rv.headers['Set-Cookie']


def test_redirect():
    rv = client.get('/redirect', headers={
        'X-XHR-Referer': '/page'
    })
    assert 'X-XHR-Redirected-To' not in rv.headers


def test_x_redirect():
    rv = client.get('/x-redirect')
    assert rv.status_code == 302

    rv = client.get('/x-redirect', headers={
        'X-XHR-Referer': '/page'
    })
    assert rv.status_code == 403

    rv = client.get('/x-redirect', headers={
        'X-XHR-Referer': 'http://example.com/'
    })
    assert rv.status_code == 403

    rv = client.get('/x-redirect', headers={
        'X-XHR-Referer': 'http://lepture.com:8000/'
    })
    assert rv.status_code == 403

    rv = client.get('/x-redirect', headers={
        'X-XHR-Referer': 'http://lepture.com/life/'
    })
    assert rv.status_code == 302
