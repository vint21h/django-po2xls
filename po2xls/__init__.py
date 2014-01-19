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

    headers = {
        'strings': [u'msgid', u'msgstr', ],
        'metadata': [u'key', u'value', ],
    }

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

    def _write_header(self, sheet, sheet_name):
        """
        Write sheet header.
        """

        header = sheet.row(0)
        for i, column in enumerate(self.headers[sheet_name]):
            header.write(i, self.headers[sheet_name][i])

    def _get_output_path(self):
        """
        Create full path for excel file to save parsed translations strings.
        """

        path, src = os.path.split(self.src)
        src, ext = os.path.splitext(src)

        return os.path.join(path, u"%s.xls" % src)

    def _write_strings(self):
        """
        Write strings sheet.
        """

        sheet = self.result.add_sheet(u'strings')
        self._write_header(sheet, 'strings')

        n_row = 1

        for entry in self.po:
            new_row = sheet.row(n_row)
            new_row.write(0, entry.msgid)
            new_row.write(1, entry.msgstr)
            n_row += 1
            sheet.flush_row_data()

    def _write_metadata(self):
        """
        Write metadata sheet.
        """

        sheet = self.result.add_sheet(u'metadata')
        self._write_header(sheet, 'metadata')

        n_row = 1

        for k in self.po.metadata:
            new_row = sheet.row(n_row)
            new_row.write(0, k)
            new_row.write(1, self.po.metadata[k])
            n_row += 1
            sheet.flush_row_data()

    def parse(self, *args, **kwargs):
        """
        Yes it is, thanks captain.
        """

        self._write_strings()
        self._write_metadata()

        # save file
        self.result.save(self.output)
