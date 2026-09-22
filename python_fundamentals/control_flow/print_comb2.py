#!/usr/bin/env python3

i = 0
j = 0
sep = ""

while i < 100:

    print("{}{:02d}".format(sep, i), end="")
    sep = ", "

    i += 1
