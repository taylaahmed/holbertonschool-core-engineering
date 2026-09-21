#!/usr/bin/env python3

def pow(a, b):
    i = 0
    total = 1
    if b > 0:
        for i in range(b):
            total *= a

    else:
        for i in range(-b):
            total *= a

        total = 1 / total

    return total
