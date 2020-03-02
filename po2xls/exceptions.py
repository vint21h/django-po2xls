# -*- coding: utf-8 -*-

# django-po2xls
# po2xls/exceptions.py


from typing import List  # pylint: disable=W0611


__all__ = [
    "ConversionError",
]  # type: List[str]


class ConversionError(Exception):
    """
    Problem while converting exception.
    """

    ...
