# -*- coding: utf-8 -*-

# po2xls
# __init__.py

import sys
import os
import logging

import polib
import xlwt

__all__ = ['management', 'models', 'views', 'PoToXls', ]


class PoToXls(object):

    logger = logging.getLogger(__name__)

    def __init__(self, src, *args, **kwargs):

        self.quiet = kwargs.pop('quiet', False)

        if os.path.exists(src):
            self.src = src
        else:
            if not self.quiet:
                sys.stderr.write(u"ERROR: File '%s' does not exists.")
            self.logger.error(u"ERROR: File '%s' does not exists.")
            sys.exit(-1)

        self.output = self._get_output_path()
        self.po = polib.pofile(self.src)
        self.result = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.result.add_sheet(u'.po')
        self._write_header()
        self.n_row = 1

    def _write_header(self):
        """
        Create header of xls file.
        """

        row0 = self.sheet.row(0)
        row0.write(0, u'msgid')
        row0.write(1, u'msgstr')

    def _get_output_path(self):
        """
        Create full path for excel file to save parsed translations strings.
        """

        path, src = os.path.split(self.src)
        src, ext = os.path.splitext(src)

        return os.path.join(path, u"%s.xls" % src)

    def parse(self, *args, **kwargs):
        """
        Yes it is, thanks captain.
        """

        for entry in self.po:
            new_row = self.sheet.row(self.n_row)
            new_row.write(0, entry.msgid)
            new_row.write(1, entry.msgstr)
            self.n_row += 1
            self.sheet.flush_row_data()

        # save file
        self.result.save(self.output)
