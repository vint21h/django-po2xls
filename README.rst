.. django-po2xls
.. README.rst

A django-po2xls documentation
=============================

    *django-po2xls is a django management command to convert project translation .po files to .xls*

.. contents::

Warning
-------
django-po2xls does not support plural.

Installation
------------
* Obtain your copy of source code from the git repository: ``git clone https://github.com/vint21h/django-po2xls.git``. Or download the latest release from https://github.com/vint21h/django-po2xls/tags/.
* Run ``python ./setup.py install`` from repository source tree or unpacked archive. Or use pip: ``pip install django-po2xls``.

Configuration
-------------
Add ``"po2xls"`` to ``settings.INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS += (
        "po2xls",
    )


Usage
-----
Just run ``po-to-xls`` django management command and .xls files dropped near all of your project .po files.

Licensing
---------
django-po2xls is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
For complete license text see COPYING file.

Contacts
--------
**Project Website**: https://github.com/vint21h/django-po2xls/

**Author**: Alexei Andrushievich <vint21h@vint21h.pp.ua>

For other authors list see AUTHORS file.
