#!/usr/bin/env python

items = [1, 2, 3, 4, 5]

def is_even(n:int) -> bool:
    return n % 2 == 0

ret = filter(is_even, items)
print(list(ret))

ret2 = filter(lambda n: n % 2 == 1, items)
print(list(ret2))

ret3 = [n for n in items if n % 2 == 0]
print(ret3)