#!/usr/bin/env python3
"""Appends a provided file"""


def append_write(filename="", text=""):
    """appends file"""

    with open(filename, 'a') as f:
        return f.write(text)
