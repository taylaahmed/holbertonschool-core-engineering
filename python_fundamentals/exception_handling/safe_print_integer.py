#!/usr/bin/env python3

def safe_print_integer(value):
    if isinstance(value, (int, float)):
        try:
            print("{:d}".format(value))
            return True
        except:
            return False
