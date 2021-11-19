# -*- coding: utf-8 -*-

# django-po2xls
# po2xls/apps.py


from typing import List

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


__all__: List[str] = ["DjangoPoToXlsConfig"]


class DjangoPoToXlsConfig(AppConfig):
    """Application config."""

    name: str = "po2xls"
    verbose_name: str = _("Convert .po to .xls")
