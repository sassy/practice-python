#!/usr/bin/env python

from functools import reduce

items = [1, 2, 3, 4, 4]
print(items)

def add(n1: int, n2: int) -> int:
    return n1 + n2

ret = reduce(add, items)
print(ret)

ret2 = reduce(lambda a, b: a * b, items)
print(ret2)