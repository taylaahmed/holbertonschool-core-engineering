#!/usr/bin/env python3

def uppercase(str):

    word = list(str)
    new = []

    for letter in word:
        ascii_value = ord(letter)
        if ascii_value >= 97 and ascii_value <= 122:
            ascii_value -= 32
            new.append(chr(ascii_value))
        else:
            new.append(letter)

    uppercase = "".join(new)
    print("{}".format(uppercase))
