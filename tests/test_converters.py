# -*- coding: utf-8 -*-

# django-po2xls
# tests/test_converters.py


import os
import pathlib
from typing import List  # pylint: disable=W0611

import xlrd
import polib
from django.test import TestCase

from po2xls.converters import PoToXls
from po2xls.exceptions import ConversionError


__all__ = ["PoToXlsTest"]  # type: List[str]


class PoToXlsTest(TestCase):
    """
    .po to .xls converter tests.
    """

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Tear down.
        """

        os.remove("po2xls/locale/uk/LC_MESSAGES/django.xls")

        super().tearDownClass()

    def test___init___raises_conversion_error_exception(self) -> None:
        """
        __init__ method must raise "ConversionError".
        """

        with self.assertRaises(expected_exception=ConversionError):
            PoToXls(src="locale/uk/LC_MESSAGES/django.po")

    def test_output(self) -> None:
        """
        output method must return original file path but with extension changed to "po".
        """

        converter = PoToXls(src="po2xls/locale/uk/LC_MESSAGES/django.po")

        result = converter.output(
            src=pathlib.Path("po2xls/locale/uk/LC_MESSAGES/django.po")
        )
        expected = pathlib.Path("po2xls/locale/uk/LC_MESSAGES/django.xls")

        self.assertEqual(first=result, second=expected)

    def test_convert__file_exists(self) -> None:
        """
        convert method must write converted data to .xls file.
        """

        PoToXls(src="po2xls/locale/uk/LC_MESSAGES/django.po").convert()

        self.assertTrue(
            expr=pathlib.Path("po2xls/locale/uk/LC_MESSAGES/django.xls").exists()
        )

    def test_convert(self) -> None:
        """
        convert method must write converted data to .xls file.
        """

        PoToXls(src="po2xls/locale/uk/LC_MESSAGES/django.po").convert()

        po = polib.pofile(
            pofile="po2xls/locale/uk/LC_MESSAGES/django.po"
        )  # type: polib.POFile
        po_metadata = [["key", "value"]] + [
            [data, po.metadata[data]] for data in po.metadata
        ]  # type: List[List[str]]
        po_strings = [["msgid", "msgstr"]] + [
            [entry.msgid, entry.msgstr] for entry in po
        ]  # type: List[List[str]]
        xls = xlrd.open_workbook(
            filename="po2xls/locale/uk/LC_MESSAGES/django.xls"
        )  # type: xlrd.Workbook
        xls_metadata = [
            xls.sheet_by_name(sheet_name=PoToXls.METADATA_SHEET_NAME).row_values(
                rowx=row_i
            )
            for row_i in range(
                0, xls.sheet_by_name(sheet_name=PoToXls.METADATA_SHEET_NAME).nrows
            )
        ]  # type: List[List[str]]
        xls_strings = [
            xls.sheet_by_name(sheet_name=PoToXls.STRINGS_SHEET_NAME).row_values(
                rowx=row_i
            )
            for row_i in range(
                0, xls.sheet_by_name(sheet_name=PoToXls.STRINGS_SHEET_NAME).nrows
            )
        ]  # type: List[List[str]]

        self.assertListEqual(list1=xls_metadata, list2=po_metadata)
        self.assertListEqual(list1=xls_strings, list2=po_strings)
