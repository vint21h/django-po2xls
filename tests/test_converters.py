# -*- coding: utf-8 -*-

# django-po2xls
# tests/test_converters.py


import os
import pathlib
from typing import List

import xlrd
import polib
from django.test import TestCase

from po2xls.converters import PoToXls
from po2xls.exceptions import ConversionError


__all__: List[str] = ["PoToXlsTest"]


class PoToXlsTest(TestCase):
    """.po to .xls converter tests."""

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down."""
        os.remove("po2xls/locale/uk/LC_MESSAGES/django.xls")

        super().tearDownClass()

    def test___init___raises_conversion_error_exception(self) -> None:
        """__init__ method must raise "ConversionError"."""
        with self.assertRaises(expected_exception=ConversionError):
            PoToXls(src="locale/uk/LC_MESSAGES/django.po")

    def test_output(self) -> None:
        """output method must return original file path but with extension changed to "po"."""  # noqa: E501,D403
        converter = PoToXls(src="po2xls/locale/uk/LC_MESSAGES/django.po")

        result = converter.output(
            src=pathlib.Path("po2xls/locale/uk/LC_MESSAGES/django.po")
        )
        expected = pathlib.Path("po2xls/locale/uk/LC_MESSAGES/django.xls")

        self.assertEqual(first=result, second=expected)

    def test_convert__file_exists(self) -> None:
        """convert method must write converted data to .xls file."""  # noqa: D403
        PoToXls(src="po2xls/locale/uk/LC_MESSAGES/django.po").convert()

        self.assertTrue(
            expr=pathlib.Path("po2xls/locale/uk/LC_MESSAGES/django.xls").exists()
        )

    def test_convert(self) -> None:
        """convert method must write converted data to .xls file."""  # noqa: D403
        PoToXls(src="po2xls/locale/uk/LC_MESSAGES/django.po").convert()

        po: polib.POFile = polib.pofile(
            pofile="po2xls/locale/uk/LC_MESSAGES/django.po"
        )
        po_metadata: List[List[str]] = [["key", "value"]] + [  # noqa: ECE001
            [data, po.metadata[data]] for data in po.metadata
        ]
        po_strings: List[List[str]] = [["msgid", "msgstr"]] + [
            [entry.msgid, entry.msgstr] for entry in po
        ]
        xls: xlrd.Workbook = xlrd.open_workbook(
            filename="po2xls/locale/uk/LC_MESSAGES/django.xls"
        )
        xls_metadata: List[List[str]] = [
            xls.sheet_by_name(sheet_name=PoToXls.METADATA_SHEET_NAME).row_values(
                rowx=row_i
            )
            for row_i in range(
                0, xls.sheet_by_name(sheet_name=PoToXls.METADATA_SHEET_NAME).nrows
            )
        ]
        xls_strings: List[List[str]] = [
            xls.sheet_by_name(sheet_name=PoToXls.STRINGS_SHEET_NAME).row_values(
                rowx=row_i
            )
            for row_i in range(
                0, xls.sheet_by_name(sheet_name=PoToXls.STRINGS_SHEET_NAME).nrows
            )
        ]

        self.assertListEqual(list1=xls_metadata, list2=po_metadata)
        self.assertListEqual(list1=xls_strings, list2=po_strings)
