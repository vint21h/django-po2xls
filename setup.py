#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-po2xls
# setup.py

from setuptools import setup, find_packages

# metadata
VERSION = (0, 2, 2)
__version__ = ".".join(map(str, VERSION))

setup(
    name="django-po2xls",
    version=__version__,
    packages=find_packages(),
    install_requires=["django-rosetta==0.7.6", "polib==1.0.6", "xlwt==1.0.0", ],
    author="Alexei Andrushievich",
    author_email="vint21h@vint21h.pp.ua",
    description="Convert gettext .po files to .xls",
    license="GPLv3 or later",
    url="https://github.com/vint21h/django-po2xls",
    download_url="https://github.com/vint21h/django-po2xls/archive/{version}.tar.gz".format(version=__version__),
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
        "Framework :: Django :: 1.5",
        "Framework :: Django :: 1.6",
        "Framework :: Django :: 1.7",
        "Framework :: Django :: 1.8",
    ]
)
