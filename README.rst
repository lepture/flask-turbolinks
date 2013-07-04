Flask-Trubolinks
================

Turbolinks for Flask.


Installation
------------

To install Flask-Turbolinks, simply::

    $ pip install Flask-Turbolinks

Or alternatively if you don't have pip::

    $ easy_install Flask-Turbolinks


Usage
-----

To enable turbolinks, you need to put `turbolinks.js`_ in the ``<head>>`` of
your html templates.


The backend flask app should be wrapped with turbolinks::

    from flask import Flask
    from flask_turbolinks import turbolinks

    app = Flask(__name__)
    # you app should has a secret key for session
    app.secret_key = 'secret')

    turbolinks(app)

And everything works now, no more configuration.

.. _`turbolinks.js`: https://github.com/rails/turbolinks


Note
----

This project does not contain the javascript code, you need to grab the code from `turbolinks.js` on GitHub. It is written in CoffeeScript, you can compile it with::

    coffee -c turbolinks.js.coffee
