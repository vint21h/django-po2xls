# -*- coding: utf-8 -*-

# django-po2xls
# po2xls/apps.py


from typing import List  # pylint: disable=W0611

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


__all__ = ["DjangoPoToXlsConfig"]  # type: List[str]


class DjangoPoToXlsConfig(AppConfig):
    """
    Application config.
    """

    name = "po2xls"  # type: str
    verbose_name = _("Convert .po to .xls")  # type: str
