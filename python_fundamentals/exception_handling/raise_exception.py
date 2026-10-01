#!/usr/bin/env python3

def raise_exception():
    a = "5"
    b = 10
    try:
        result = a + b
        print("{}".format(result))
    except (TypeError):
        print("A type error occured")