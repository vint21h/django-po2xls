# -*- coding: utf-8 -*-

# django-po2xls
# po2xls/management/commands/po2xls.py

from __future__ import unicode_literals
from optparse import make_option

from django.core.management.base import BaseCommand
from django.conf import settings

from rosetta.poutil import find_pos

from po2xls import PoToXls


class Command(BaseCommand):
    """
    Convert project translation files to excel.
    """

    _all = "all"

    option_list = BaseCommand.option_list + (
        make_option("--language", "-l", dest="language", help="Language", default=_all),
        make_option("--quiet", "-q", dest="quiet", help="Be quiet", default=False, action="store_true"),
    )

    def handle(self, *args, **kwargs):

        if kwargs["language"] == self._all:
            for language in dict(settings.LANGUAGES).keys():
                self._parse(language)
        else:
            self._parse(kwargs["language"])

    def _parse(self, language, *args, **kwargs):

        for f in find_pos(language):
            PoToXls(f, **kwargs).parse()
