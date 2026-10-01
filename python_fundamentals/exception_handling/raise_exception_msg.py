#!/usr/bin/env python3

def raise_exception_msg(message=""):
    try:
        print("{}".format(message))
    except (NameError):
        print("Exception has been raised")
