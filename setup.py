#!/usr/bin/env python
# coding=utf-8

import os
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))
PACKAGE_NAME = 'mailjet_rest'

import ipdb; ipdb.set_trace()
# Dynamically calculate the version based on mailjet_rest.VERSION.
version = __import__('mailjet_rest').get_version()

setup(
    name=PACKAGE_NAME,
    version=version,
    author='starenka',
    author_email='starenka0@gmail.com',
    maintainer='Mailjet',
    maintainer_email='api@mailjet.com',
    download_url='https://github.com/mailjet/mailjet-apiv3-python/releases/tag/v' + version,
    url='https://github.com/mailjet/mailjet-apiv3-python',
    description=('Mailjet V3 API wrapper'),
    classifiers=['Development Status :: 3 - Alpha',
                 'Environment :: Console',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: GNU General Public License (GPL)',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Topic :: Utilities'],
    license='MIT',
    keywords='Mailjet API v3 / v3.1 Python Wrapper',

    include_package_data=True,
    install_requires=['requests>=2.4.3'],
    tests_require=['unittest'],
    entry_points={},
    packages=['mailjet_rest'],
)
