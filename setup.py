#!/usr/bin/env python
# coding=utf-8

import os
import re
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))
PACKAGE_NAME = 'mailjet_rest'

# Taken from https://stackoverflow.com/a/39671214/1506051
__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
    open('mailjet_rest/_version.py').read()).group(1)

setup(
    name=PACKAGE_NAME,
    version=__version__,
    author='starenka',
    author_email='starenka0@gmail.com',
    maintainer='Mailjet',
    maintainer_email='api@mailjet.com',
    download_url='https://github.com/mailjet/mailjet-apiv3-python/releases/tag/v'+__version__,
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
                 'Programming Language :: Python :: 3.2',
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
