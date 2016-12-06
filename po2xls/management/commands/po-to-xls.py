# -*- coding: utf-8 -*-

# django-po2xls
# po2xls/management/commands/po2xls.py

from __future__ import unicode_literals

from django.core.management.base import BaseCommand
from django.conf import settings

from rosetta.poutil import find_pos

from po2xls.utils import PoToXls


class Command(BaseCommand):
    """
    Convert project translation files to excel.
    """

    all = "all"

    def add_arguments(self, parser):

        parser.add_argument("--language", "-l", dest="language", help="Language", default=all)
        parser.add_argument("--quiet", "-q", dest="quiet", help="Be quiet", default=False, action="store_true")

    def handle(self, *args, **kwargs):

        language = kwargs.pop("language")

        if all([language == self.all, settings.LANGUAGES, ]):
            for language in list(dict(settings.LANGUAGES).keys()):
                self.convert(language=language, **kwargs)
        else:
            self.convert(language=language, **kwargs)

    def convert(self, language, *args, **kwargs):
        """
        Run converter.
        Args:
            language: (unicode) language code.
        """

        for f in find_pos(language):
            PoToXls(src=f, **kwargs).convert()
