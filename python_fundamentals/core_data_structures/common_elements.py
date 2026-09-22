#!/usr/bin/env python3

def common_elements(set_1, set_2):
    new_set = []

    for word_1 in set_1:
        for word_2 in set_2:
            if word_1 == word_2:
                new_set.append(word_1)

    return new_set
