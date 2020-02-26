# -*- coding: utf-8 -*-

# django-po2xls
# po2xls/utils.py


import pathlib
from typing import Any, Dict, List  # pylint: disable=W0611

import polib
import xlwt

from po2xls.exceptions import ConversionError


__all__ = [
    "PoToXls",
]  # type: List[str]


class PoToXls:
    """
    .po to .xls converter.
    """

    HEADERS = {
        "strings": ["msgid", "msgstr"],
        "metadata": ["key", "value"],
    }

    def __init__(self, src: str, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        """
        Setup conversion.

        :param src: path to ".po" file.
        :type src: str.
        :param args: additional args.
        :type args: List[Any].
        :param kwargs: additional args.
        :type kwargs: Dict[str, Any].
        :return: nothing.
        :rtype: None.
        """

        self.src = pathlib.Path(src)  # type: pathlib.Path

        if not self.src.exists():
            raise ConversionError(f"ERROR: File '{src}' does not exists.")

        try:
            self.po = polib.pofile(self.src)  # type: polib.POFile
        except (ValueError, IOError) as error:
            raise ConversionError(f"ERROR: '{src}' - file problem: {error}")

        self.result = xlwt.Workbook(encoding="utf-8")  # type: xlwt.Workbook

    def header(self, sheet: xlwt.Worksheet, name: str) -> None:
        """
        Write sheet header.

        :param sheet: instance of xlwt sheet to write header to.
        :type sheet: xlwt.Worksheet.
        :param name: sheet name.
        :type name: str.
        """

        header = sheet.row(0)  # type: xlwt.Row

        for i, column in enumerate(  # pylint: disable=W0612  # noqa: B007  # noqa: E501
            self.HEADERS[name]
        ):
            header.write(i, self.HEADERS[name][i])

        sheet.flush_row_data()

    @staticmethod
    def output(src: pathlib.Path) -> pathlib.Path:
        """
        Create full path for excel file to save parsed translations strings.

        :param src: path to .po file.
        :type src: pathlib.Path.
        :return: path to .xls file.
        :rtype: pathlib.Path.
        """

        return src.parent.joinpath(f"{src.stem}.xls")

    def strings(self) -> None:
        """
        Write strings sheet.

        :return: nothing.
        :rtype: None.
        """

        sheet = self.result.add_sheet("strings")  # type: xlwt.Worksheet
        self.header(sheet, "strings")

        n_row = 1  # type: int  # row number (first after header)

        for entry in self.po:
            row = sheet.row(n_row)  # type: xlwt.Row
            row.write(0, entry.msgid)
            row.write(1, entry.msgstr)
            n_row += 1
            sheet.flush_row_data()

    def metadata(self) -> None:
        """
        Write metadata sheet.

        :return: nothing.
        :rtype: None.
        """

        sheet = self.result.add_sheet("metadata")  # type: xlwt.Worksheet
        self.header(sheet, "metadata")

        n_row = 1  # type: int  # row number (first after header)

        for data in self.po.metadata:
            row = sheet.row(n_row)  # type: xlwt.Row
            row.write(0, data)
            row.write(1, self.po.metadata[data])
            n_row += 1
            sheet.flush_row_data()

    def convert(self, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        """
        Yes it is, thanks captain.

        :param args: additional args.
        :type args: List[Any].
        :param kwargs: additional args.
        :type kwargs: Dict[str, Any].
        :return: nothing.
        :rtype: None.
        """

        self.strings()
        self.metadata()
        self.result.save(self.output(src=self.src))
