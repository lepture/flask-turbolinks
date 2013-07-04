from flask import Flask, render_template, redirect
from flask_turbolinks import turbolinks


app = Flask(__name__)
app.secret_key = 'secret'

turbolinks(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/page')
def page():
    return render_template('page.html')


@app.route('/redirect')
def in_redirect():
    return redirect('/page')


@app.route('/x-redirect')
def x_redirect():
    return redirect('http://lepture.com')


if __name__ == '__main__':
    app.debug = True
    app.run()
