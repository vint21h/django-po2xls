.. django-po2xls
.. README.rst

A django-po2xls documentation
=============================

|Travis|_ |Coveralls|_ |Requires|_ |pypi-license|_ |pypi-version|_ |pypi-python-version|_ |pypi-django-version|_ |pypi-format|_ |pypi-wheel|_ |pypi-status|_

    *django-po2xls is a Django management command to convert project translation .po files to .xls*

.. contents::

Warning
-------
django-po2xls does not support plural.

Installation
------------
* Obtain your copy of source code from the git repository: ``$ git clone https://github.com/vint21h/django-po2xls.git``. Or download the latest release from https://github.com/vint21h/django-po2xls/tags/.
* Run ``$ python ./setup.py install`` from the repository source tree or unpacked archive. Or use pip: ``$ pip install django-po2xls``.

Configuration
-------------
Add ``"po2xls"`` to ``settings.INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS += [
        "po2xls",
    ]


Usage
-----
Just run: ``$ python ./manage.py po-to-xls`` Django management command from project folder and .xls files will be dropped near all of your project .po files.

Licensing
---------
django-po2xls is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
For complete license text see COPYING file.

Contacts
--------
**Project Website**: https://github.com/vint21h/django-po2xls/

**Author**: Alexei Andrushievich <vint21h@vint21h.pp.ua>

For other authors list see AUTHORS file.


.. |Travis| image:: https://travis-ci.org/vint21h/django-po2xls.svg?branch=master
    :alt: Travis
.. |Coveralls| image:: https://coveralls.io/repos/github/vint21h/django-po2xls/badge.svg?branch=master
    :alt: Coveralls
.. |Requires| image:: https://requires.io/github/vint21h/django-po2xls/requirements.svg?branch=master
    :alt: Requires
.. |pypi-license| image:: https://img.shields.io/pypi/l/django-po2xls
    :alt: License
.. |pypi-version| image:: https://img.shields.io/pypi/v/django-po2xls
    :alt: Version
.. |pypi-django-version| image:: https://img.shields.io/pypi/djversions/django-po2xls
    :alt: Supported Django version
.. |pypi-python-version| image:: https://img.shields.io/pypi/pyversions/django-po2xls
    :alt: Supported Python version
.. |pypi-format| image:: https://img.shields.io/pypi/format/django-po2xls
    :alt: Package format
.. |pypi-wheel| image:: https://img.shields.io/pypi/wheel/django-po2xls
    :alt: Python wheel support
.. |pypi-status| image:: https://img.shields.io/pypi/status/django-po2xls
    :alt: Package status
.. _Travis: https://travis-ci.org/vint21h/django-po2xls/
.. _Coveralls: https://coveralls.io/github/vint21h/django-po2xls?branch=master
.. _Requires: https://requires.io/github/vint21h/django-po2xls/requirements/?branch=master
.. _pypi-license: https://pypi.org/project/django-po2xls/
.. _pypi-version: https://pypi.org/project/django-po2xls/
.. _pypi-django-version: https://pypi.org/project/django-po2xls/
.. _pypi-python-version: https://pypi.org/project/django-po2xls/
.. _pypi-format: https://pypi.org/project/django-po2xls/
.. _pypi-wheel: https://pypi.org/project/django-po2xls/
.. _pypi-status: https://pypi.org/project/django-po2xls/
