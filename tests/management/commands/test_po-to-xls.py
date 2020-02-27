# -*- coding: utf-8 -*-

# django-po2xls
# tests/management/commands/test_po-to-xls.py


from importlib import import_module
import os
import pathlib
from typing import List  # pylint: disable=W0611

from django.test import TestCase


Command = import_module("po2xls.management.commands.po-to-xls").Command  # type: ignore


__all__ = ["CommandTest"]  # type: List[str]


class CommandTest(TestCase):
    """
    po-to-xls management command tests.
    """

    @classmethod
    def tearDownClass(cls):
        """
        Tear down.
        """

        os.remove("po2xls/locale/uk/LC_MESSAGES/django.xls")

        super().tearDownClass()

    def test_convert(self):
        """
        convert method must write converted data to .xls files for chosen locale.
        """

        Command().convert(locale="uk")

        self.assertTrue(
            expr=pathlib.Path("po2xls/locale/uk/LC_MESSAGES/django.xls").exists()
        )
