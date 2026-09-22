#!/usr/bin/env python3

i = 0
sep = ""

while i < 10:
    j = 0
    while j < 10:
        print("{}{}{}".format(sep, i, j), end="")
        sep = ", "
        j += 1
    i += 1
