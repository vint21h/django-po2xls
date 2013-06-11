.. po2xls
.. README.rst

A django-po2xls documentation
===================================

    *po2xls is a django management command to convert project translation .po filex to .xls*

.. contents::

Installation
------------
* Obtain your copy of source code from git repository: ``git clone https://github.com/vint21h/django-po2xls.git``. Or download latest release from https://github.com/vint21h/django-po2xls/tags.
* Run ``python ./setup.py install`` from repository source tree or unpacked archive. Or use pip: ``pip install django-po2xls``.

Configuration
-------------
List this application in the INSTALLED_APPS portion of your settings file. Your settings file might look something like:

INSTALLED_APPS = (
    # ...
    'po2xls',

)

Use
---
Just run ``./manage.py po-to-xls`` and .xls files dropped near your project .po files.

Licensing
---------
django-po2xls is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
For complete license text see COPYING file.

Contacts
--------
**Project Website**: https://github.com/vint21h/django-po2xls

**Author**: Alexei Andrushievich <vint21h@vint21h.pp.ua>
