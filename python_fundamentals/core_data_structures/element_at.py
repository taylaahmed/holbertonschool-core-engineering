#!/usr/bin/env python3

def element_at(my_list, idx):

    if idx >= 0 and idx < len(my_list):
        return("{}".format(my_list[idx]))
    else:
        return("None")
