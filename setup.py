#!/usr/bin/env python

from setuptools import setup

setup(
    name='pkg_orphan',
    version='1.0',
    description='Find installed pkgsrc packages which are not dependencies of any other packages (orphans)',
    author='Luke Maurits',
    author_email='luke@maurits.id.au',
    url='https://github.com/lmaurits/pkg_orphan',
    license="BSD (3 clause)",
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: BSD License',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Systems Administration',
    ],
    scripts=['pkg_orphan',],
)
