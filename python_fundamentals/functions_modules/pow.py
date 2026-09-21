#!/usr/bin/env python3

def pow(a, b):
    i = 0
    total = 1
    if b > 0:
        while i < b:
            total *= a
            i += 1
    else:
        while i > b:
            total /= a
            i -= 1
    return total
