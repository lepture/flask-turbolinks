#!/usr/bin/env python
# coding: utf-8


from setuptools import setup

setup(
    name='Flask-Turbolinks',
    version='0.1.1',
    url='https://github.com/lepture/flask-turbolinks',
    author='Hsiaoming Yang',
    author_email='me@lepture.com',
    description='Turbolinks for Flask.',
    long_description=open('README.rst').read(),
    license=open('LICENSE').read(),
    py_modules=['flask_turbolinks'],
    platforms='any',
    install_requires=['Flask'],
    tests_require=['nose'],
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
