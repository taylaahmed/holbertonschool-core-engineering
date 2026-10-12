#!/usr/bin/env python3
"""Write into new file"""


def write_file(filename="", text=""):
    """write to file"""

    with open(filename, 'w') as f:
        return f.write(text)
