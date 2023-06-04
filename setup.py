#!/usr/bin/env python3
from setuptools import setup

setup(
        name = 'bibskiptex',
        version = '0.1',
        description = 'Bibtex alternative to produce .bbl without .aux',
        author = 'Jakub Opršal',
        author_email = 'git@jakub-oprsal.info',
        license = 'MIT',
        py_modules = ['bibskiptex'],
        install_requires = ['pybtex']
)
