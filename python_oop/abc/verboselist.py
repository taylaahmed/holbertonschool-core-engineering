#!/usr/bin/env python3
"""Verbose List"""


class VerboseList(list):

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items")

    def remove(self, value):
        super().remove(value)
        print(f"Removed [{value}] from the list")

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped [{item}] from the list")
        return item
