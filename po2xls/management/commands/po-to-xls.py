# -*- coding: utf-8 -*-

# po2xls
# management/commands/po2xls.py

from optparse import make_option

from django.core.management.base import BaseCommand
from django.conf import settings

from rosetta.poutil import find_pos

from po2xls import PoToXls


class Command(BaseCommand):
    """
    Convert project translation files to excel.
    """

    option_list = BaseCommand.option_list + (
        make_option('--language', '-l', dest='language', help=u'Language', default=u'all'),
        make_option('--quiet', '-q', dest='quiet', help=u'Be quiet', default=False, action="store_true"),
    )

    def handle(self, *args, **options):

        if options['language'] == u"all":
            for lang in settings.LANGUAGES:
                self._parse(lang)
        else:
            self._parse(options['language'])

    def _parse(self, lang):

        for f in find_pos(lang[0]):
            PoToXls(f).parse()
