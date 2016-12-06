# -*- coding: utf-8 -*-

# django-po2xls
# po2xls/utils.py

from __future__ import unicode_literals
import sys
import os
import logging

import polib
import xlwt


__all__ = [
    "PoToXls",
]


class PoToXls(object):

    logger = logging.getLogger(__name__)

    headers = {
        "strings": [
            "msgid",
            "msgstr",
        ],
        "metadata": [
            "key",
            "value",
        ],
    }

    def __init__(self, src, *args, **kwargs):
        """
        Init conversion.
        Args:
            src: (unicode or string) path to ".po" file.
        """
        self.quiet = kwargs.pop("quiet", False)

        if os.path.exists(src):
            self.src = src
        else:
            if not self.quiet:
                sys.stderr.write("ERROR: File '{src}' does not exists.".format(**{"src": src, }))
            self.logger.error("ERROR: File '{src}' does not exists.".format(**{"src": src, }))
            sys.exit(-1)

        self.po = polib.pofile(self.src)
        self.result = xlwt.Workbook(encoding="utf-8")

    def header(self, sheet, name):
        """
        Write sheet header.
        Args:
            sheet: (xlwt.Worksheet.Worksheet) instance of xlwt sheet.
            name: (unicode) name of sheet.
        """

        header = sheet.row(0)
        for i, column in enumerate(self.headers[name]):
            header.write(i, self.headers[name][i])

    def output(self):
        """
        Create full path for excel file to save parsed translations strings.
        Returns:
            unicode: full path for excel file to save parsed translations strings.
        """

        path, src = os.path.split(self.src)
        src, ext = os.path.splitext(src)

        return os.path.join(path, "{src}.xls".format(**{"src": src, }))

    def strings(self):
        """
        Write strings sheet.
        """

        sheet = self.result.add_sheet("strings")
        self.header(sheet, "strings")

        n_row = 1  # row number

        for entry in self.po:
            row = sheet.row(n_row)
            row.write(0, entry.msgid)
            row.write(1, entry.msgstr)
            n_row += 1
            sheet.flush_row_data()

    def metadata(self):
        """
        Write metadata sheet.
        """

        sheet = self.result.add_sheet("metadata")
        self.header(sheet, "metadata")

        n_row = 1  # row number

        for k in self.po.metadata:
            row = sheet.row(n_row)
            row.write(0, k)
            row.write(1, self.po.metadata[k])
            n_row += 1
            sheet.flush_row_data()

    def convert(self, *args, **kwargs):
        """
        Yes it is, thanks captain.
        """

        self.strings()
        self.metadata()

        # save file
        self.result.save(self.output())
