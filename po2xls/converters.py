# -*- coding: utf-8 -*-

# django-po2xls
# po2xls/converters.py


from pathlib import Path
from typing import Any, Dict, List  # pylint: disable=W0611

import xlwt
import polib

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
    METADATA_SHEET_NAME = "metadata"
    STRINGS_SHEET_NAME = "strings"

    def __init__(self, src: str, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        """
        Setup conversion.

        :param src: path to ".po" file
        :type src: str
        :param args: additional args
        :type args: List[Any]
        :param kwargs: additional args
        :type kwargs: Dict[str, Any]
        :raises ConversionError: raised when file does not exists, IO errors or file format problems  # noqa: E501
        """

        self.src = Path(src)  # type: Path

        if not self.src.exists():
            raise ConversionError(f"ERROR: File '{src}' does not exists.")

        try:
            self.po = polib.pofile(pofile=str(self.src))  # type: polib.POFile
        except (ValueError, IOError) as error:
            raise ConversionError(f"ERROR: '{src}' - file problem: {error}")

        self.result = xlwt.Workbook(encoding="utf-8")  # type: xlwt.Workbook

    def header(self, sheet: xlwt.Worksheet, name: str) -> None:
        """
        Write sheet header.

        :param sheet: instance of xlwt sheet to write header to
        :type sheet: xlwt.Worksheet
        :param name: sheet name
        :type name: str
        """

        header = sheet.row(0)  # type: xlwt.Row

        for i, column in enumerate(  # pylint: disable=W0612  # noqa: B007  # noqa: E501
            self.HEADERS[name]
        ):
            header.write(i, self.HEADERS[name][i])

        sheet.flush_row_data()

    @staticmethod
    def output(src: Path) -> Path:
        """
        Create full path for excel file to save parsed translations strings.

        :param src: path to .po file
        :type src: Path
        :return: path to .xls file
        :rtype: Path
        """

        return src.parent.joinpath(f"{src.stem}.xls")

    def strings(self) -> None:
        """
        Write strings sheet.
        """

        sheet = self.result.add_sheet(self.STRINGS_SHEET_NAME)  # type: xlwt.Worksheet
        self.header(sheet=sheet, name=self.STRINGS_SHEET_NAME)

        row_i = 1  # type: int  # row number (first after header)

        for entry in self.po:
            row = sheet.row(indx=row_i)  # type: xlwt.Row
            row.write(0, entry.msgid)
            row.write(1, entry.msgstr)
            row_i += 1
            sheet.flush_row_data()

    def metadata(self) -> None:
        """
        Write metadata sheet.
        """

        sheet = self.result.add_sheet(
            sheetname=self.METADATA_SHEET_NAME
        )  # type: xlwt.Worksheet
        self.header(sheet=sheet, name=self.METADATA_SHEET_NAME)

        row_i = 1  # type: int  # row number (first after header)

        for data in self.po.metadata:
            row = sheet.row(indx=row_i)  # type: xlwt.Row
            row.write(0, data)
            row.write(1, self.po.metadata[data])
            row_i += 1
            sheet.flush_row_data()

    def convert(self, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        """
        Yes it is, thanks captain.

        :param args: additional args
        :type args: List[Any]
        :param kwargs: additional args
        :type kwargs: Dict[str, Any]
        """

        self.strings()
        self.metadata()
        self.result.save(filename_or_stream=self.output(src=self.src))
