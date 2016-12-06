# -*- coding: utf-8 -*-

# django-po2xls
# po2xls/apps.py

from __future__ import unicode_literals

from django.apps import AppConfig


__all__ = [
    "Config",
]


class Config(AppConfig):

    name = "po2xls"
    verbose_name = ".po to .xls"
