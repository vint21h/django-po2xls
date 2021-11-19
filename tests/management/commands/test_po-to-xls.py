# -*- coding: utf-8 -*-

# django-po2xls
# tests/management/commands/test_po-to-xls.py


import os
import pathlib
from typing import List
from importlib import import_module

from django.test import TestCase


# po-to-xls management command imported on the fly
# because we can't import something from the module that contains "-"
Command = import_module("po2xls.management.commands.po-to-xls").Command  # type: ignore


__all__: List[str] = ["CommandTest"]


class CommandTest(TestCase):
    """po-to-xls management command tests."""

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down."""
        os.remove("po2xls/locale/uk/LC_MESSAGES/django.xls")
        os.remove("po2xls/locale/en/LC_MESSAGES/django.xls")

        super().tearDownClass()

    def test_convert(self) -> None:
        """convert method must write converted data to .xls files for chosen locale."""  # noqa: D403,E501
        Command().convert(locale="uk")

        self.assertTrue(
            expr=pathlib.Path("po2xls/locale/uk/LC_MESSAGES/django.xls").exists()
        )

    def test_convert__all(self) -> None:
        """convert method must write converted data to .xls files for all locales."""  # noqa: D403,E501
        Command().handle()

        self.assertTrue(
            expr=pathlib.Path("po2xls/locale/en/LC_MESSAGES/django.xls").exists()
        )
        self.assertTrue(
            expr=pathlib.Path("po2xls/locale/uk/LC_MESSAGES/django.xls").exists()
        )
