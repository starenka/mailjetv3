#!/usr/bin/env python
# coding=utf-8

import sys
import os
import re
from setuptools import setup
from setuptools.command.test import test as TestCommand

HERE = os.path.abspath(os.path.dirname(__file__))
PACKAGE_NAME = 'mailjet_rest'
VERSION = 'v1.0.5'

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author='starenka',
    author_email='starenka0@gmail.com',
    maintainer='Guillaume Badi',
    maintainer_email='gbadi@mailjet.com',
    download_url='https://github.com/mailjet/mailjet-apiv3-python/releases/tag/v1.0.5',
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
                 'Topic :: Utilities'],
    license='GPLv3',
    keywords='mailjet api wrapper email client',

    include_package_data=True,
    install_requires=['requests>=2.4.3'],
    tests_require=['unittest'],
    entry_points={},
)
