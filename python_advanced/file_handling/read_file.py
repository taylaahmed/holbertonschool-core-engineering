#!/usr/bin/env python3
"""Reading into and printing from file"""


def read_file(filename=""):
    """read and print file"""

    with open(filename, 'r') as f:
        f_content = f.read()
        print(f_content, end="")
