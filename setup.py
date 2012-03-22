#!/usr/bin/env python
from distutils.core import setup

version='1.0.1'

setup(
    name='funny-codes',
    version=version,
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',

    packages=['funny_codes'],

    url='https://bitbucket.org/kmike/funny-codes/',
    license = 'MIT license',
    description = "Generate randoms strings of a given pattern",

    long_description = open('README.rst').read(),

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
