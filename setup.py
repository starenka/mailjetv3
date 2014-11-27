#!/usr/bin/env python
# coding=utf-8

import sys
import os
import re
from setuptools import setup
from setuptools.command.test import test as TestCommand

HERE = os.path.abspath(os.path.dirname(__file__))
PACKAGE_NAME = 'mailjet'

with open(os.path.join(HERE, 'README.md')) as fp:
    README = fp.read()
with open(os.path.join(HERE, PACKAGE_NAME, '__init__.py')) as fp:
    VERSION = re.search("__version__ = '([^']+)'", fp.read()).group(1)


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author='starenka',
    author_email='starenka0@gmail.com',
    maintainer='starenka',
    maintainer_email='starenka0gmail.com',
    url='https://FIXME',
    description=('Simple Mailjet V3 API wrapper'),
    long_description=README,
    classifiers=['Development Status :: 3 - Alpha',
                 'Environment :: Console',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: GNU General Public License (GPL)',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Utilities'],
    license='GPLv3',
    keywords='mailjet api wrapper',

    packages=[PACKAGE_NAME],
    package_data={'': ['README.md', 'tests', '*.ini'], PACKAGE_NAME: []},
    include_package_data=True,
    install_requires=['requests>=2.4.3'],
    tests_require=['pytest'],
    cmdclass = {'test': PyTest},
    entry_points={},
)
