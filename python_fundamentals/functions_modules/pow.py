#!/usr/bin/env python3

def pow(a, b):
    i = 0
    total = 1
    while i < b:
        total *= a
        i += 1

    return total
