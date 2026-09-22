#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):

    for lines in matrix:
        sep = ""
        for number in lines:
            print("{}{:d}".format(sep, number), end="")
            sep = " "
        print("\n", end="")
