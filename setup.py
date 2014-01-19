#!/usr/bin/env python
# -*- coding: utf-8 -*-

# po2xls
# setup.py

from setuptools import setup, find_packages

# metadata
VERSION = (0, 1, 0)
__version__ = '.'.join(map(str, VERSION))

setup(
    name="django-po2xls",
    version=__version__,
    packages=find_packages(),
    install_requires=['django-rosetta==0.6.8', 'polib==1.0.3', 'xlwt==0.7.4', ],
    author="Alexei Andrushievich",
    author_email="vint21h@vint21h.pp.ua",
    description="Convert gettext .po files to .xls",
    license="GPLv3 or later",
    url="https://github.com/vint21h/django-po2xls",
    download_url="https://github.com/vint21h/django-po2xls/archive/%s.tar.gz" % __version__,
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Environment :: Console",
        "Environment :: Plugins",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Unix",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities",
    ]
)
