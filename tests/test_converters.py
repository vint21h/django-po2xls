# -*- coding: utf-8 -*-

# django-po2xls
# tests/test_converters.py


import os
import pathlib
from typing import List  # pylint: disable=W0611

from django.test import TestCase
import polib
import xlrd

from po2xls.converters import PoToXls
from po2xls.exceptions import ConversionError


__all__ = ["PoToXlsTest"]  # type: List[str]


class PoToXlsTest(TestCase):
    """
    .po to .xls converter tests.
    """

    @classmethod
    def tearDownClass(cls):
        """
        Tear down.
        """

        os.remove("po2xls/locale/uk/LC_MESSAGES/django.xls")

        super().tearDownClass()

    def test___init___raises_conversion_error_exception(self):
        """
        __init__ method must raise "ConversionError".
        """

        with self.assertRaises(expected_exception=ConversionError):
            PoToXls(src="locale/uk/LC_MESSAGES/django.po")

    def test_output(self):
        """
        output method must return original file path but with extension changed to "po".
        """

        converter = PoToXls(src="po2xls/locale/uk/LC_MESSAGES/django.po")

        result = converter.output(
            src=pathlib.Path("po2xls/locale/uk/LC_MESSAGES/django.po")
        )
        expected = pathlib.Path("po2xls/locale/uk/LC_MESSAGES/django.xls")

        self.assertEqual(first=result, second=expected)

    def test_convert__file_exists(self):
        """
        convert method must write converted data to .xls file.
        """

        PoToXls(src="po2xls/locale/uk/LC_MESSAGES/django.po").convert()

        self.assertTrue(
            expr=pathlib.Path("po2xls/locale/uk/LC_MESSAGES/django.xls").exists()
        )

    def test_convert(self):
        """
        convert method must write converted data to .xls file.
        """

        PoToXls(src="po2xls/locale/uk/LC_MESSAGES/django.po").convert()

        po = polib.pofile(
            "po2xls/locale/uk/LC_MESSAGES/django.po"
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
            xls.sheet_by_name("metadata").row_values(row_i)
            for row_i in range(0, xls.sheet_by_name("metadata").nrows)
        ]  # type: List[List[str]]
        xls_strings = [
            xls.sheet_by_name("strings").row_values(row_i)
            for row_i in range(0, xls.sheet_by_name("strings").nrows)
        ]  # type: List[List[str]]

        self.assertListEqual(list1=xls_metadata, list2=po_metadata)
        self.assertListEqual(list1=xls_strings, list2=po_strings)
