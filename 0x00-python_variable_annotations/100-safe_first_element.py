#!/usr/bin/env python3
"""Corrected duck-typed annotations"""


import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """Duck typing"""
    if lst:
        return lst[0]
    else:
        return None
