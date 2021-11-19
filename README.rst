.. django-po2xls
.. README.rst

A django-po2xls documentation
=============================

|GitHub|_ |Coveralls|_ |pypi-license|_ |pypi-version|_ |pypi-python-version|_ |pypi-django-version|_ |pypi-format|_ |pypi-wheel|_ |pypi-status|_

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

Contributing
------------
1. `Fork it <https://github.com/vint21h/django-security-txt/>`_
2. Install `GNU Make <https://www.gnu.org/software/make/>`_
3. Install and configure `pyenv <https://github.com/pyenv/pyenv/>`_ and `pyenv-virtualenv plugin <https://github.com/pyenv/pyenv-virtualenv/>`_
4. Install and configure `direnv <https://github.com/direnv/direnv/>`_
5. Create environment config from example

.. code-block:: bash

    cp .env.example .env

6. Install development dependencies:

.. code-block:: bash

    make install

7. Create your fix/feature branch:

.. code-block:: bash

    git checkout -b my-new-fix-or-feature

8. Check code style and moreover:

.. code-block:: bash

    make check

9. Run tests:

.. code-block:: bash

    make test

10. Push to the branch:

.. code-block:: bash

    git push origin my-new-fix-or-feature

11. `Create a new Pull Request <https://github.com/vint21h/django-security-txt/compare/>`_

Licensing
---------
django-po2xls is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
For complete license text see COPYING file.

Contacts
--------
**Project Website**: https://github.com/vint21h/django-po2xls/

**Author**: Alexei Andrushievich <vint21h@vint21h.pp.ua>

For other authors list see AUTHORS file.


.. |GitHub| image:: https://github.com/vint21h/django-po2xls/workflows/build/badge.svg
    :alt: GitHub
.. |Coveralls| image:: https://coveralls.io/repos/github/vint21h/django-po2xls/badge.svg?branch=master
    :alt: Coveralls
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
.. _GitHub: https://github.com/vint21h/django-po2xls/actions/
.. _Coveralls: https://coveralls.io/github/vint21h/django-po2xls?branch=master
.. _pypi-license: https://pypi.org/project/django-po2xls/
.. _pypi-version: https://pypi.org/project/django-po2xls/
.. _pypi-django-version: https://pypi.org/project/django-po2xls/
.. _pypi-python-version: https://pypi.org/project/django-po2xls/
.. _pypi-format: https://pypi.org/project/django-po2xls/
.. _pypi-wheel: https://pypi.org/project/django-po2xls/
.. _pypi-status: https://pypi.org/project/django-po2xls/
