#!/usr/bin/env python3

def raise_exception():
    a = "Hello"
    try:
        print("{:d}".format(a))
    except (TypeError):
        print("A type error occured")