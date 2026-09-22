#!/usr/bin/env python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    highest = 0

    for key, value in a_dictionary.items():
        if value > highest:
            highest = value
            name = key
    return name
