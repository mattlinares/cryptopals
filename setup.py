# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import cryptpals
version = cryptopals.__version__

setup(
    name='cryptopals',
    version=version,
    author='',
    author_email='info@cryptopals.org',
    packages=[
        'cryptopals',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['cryptopals/manage.py'],
)