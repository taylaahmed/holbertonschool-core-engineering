#!/usr/bin/env python3

i = 0
sep = ""


while i < 100:
    j = 0
    unique = True
    while j <= i:
        numComp = sorted("{:02d}".format(j))
        original = sorted("{:02d}".format(i))

        if numComp == original or original[0] == original[1]:
            unique = False
        j += 1

    if unique:
        print("{}{:02d}".format(sep, i), end="")
        sep = ", "

    i += 1

print("\n", end="")
