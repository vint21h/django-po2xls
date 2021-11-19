# -*- coding: utf-8 -*-

# django-po2xls
# po2xls/exceptions.py


from typing import List


__all__: List[str] = [
    "ConversionError",
]


class ConversionError(Exception):
    """Problem while converting exception."""

    ...
