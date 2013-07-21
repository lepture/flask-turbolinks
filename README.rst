Flask-Turbolinks
================

.. image:: https://travis-ci.org/lepture/flask-turbolinks.png?branch=master
        :target: https://travis-ci.org/lepture/flask-turbolinks
.. image:: https://coveralls.io/repos/lepture/flask-turbolinks/badge.png?branch=master
        :target: https://coveralls.io/r/lepture/flask-turbolinks

Turbolinks for Flask.


Turbolinks
----------

Turbolinks makes following links in your web application faster. For more
information, visit the original rails repo: `turbolinks.js`_.


Installation
------------

To install Flask-Turbolinks, simply::

    $ pip install Flask-Turbolinks

Or alternatively if you don't have pip::

    $ easy_install Flask-Turbolinks


Usage
-----

To enable turbolinks, you need to put `turbolinks.js`_ in the ``<head>`` of
your html templates.


The backend flask app should be wrapped with turbolinks::

    from flask import Flask
    from flask_turbolinks import turbolinks

    app = Flask(__name__)
    # you app should has a secret key for session
    app.secret_key = 'secret'

    turbolinks(app)

And everything works now, no more configuration.

.. _`turbolinks.js`: https://github.com/rails/turbolinks


Note
----

You can install the javascript code with component::

    $ component install lepture/flask-turbolinks

You can also grab the code from `turbolinks.js` on GitHub. It is written in CoffeeScript, you can compile it with::

    coffee -c turbolinks.js.coffee


Demo
----

There is a demo in the ``example`` directory, start a server and open the
url with Chrome. View the requests with developer tools of Chrome.


Credits
-------

Thanks for rails, thanks for the help of Rei_.

.. _Rei: https://github.com/chloerei


Changelog
---------

We keep the changelog on `GitHub releases`_.

.. _`GitHub releases`: https://github.com/lepture/flask-turbolinks/releases
