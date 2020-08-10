#!/usr/bin/env python

items = [1, 2, 3]
print(items)

def plus(n: int) -> int:
    return n + 10

ret = map(plus, items)
print(list(ret))

ret2 = map(lambda n: n + 11, items)
print(list(ret2))

ret3 = [i + 12 for i in items]
print(ret3)