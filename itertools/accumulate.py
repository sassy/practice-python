#!/usr/bin/env python

from itertools import accumulate
from operator import mul

def main():
    list = accumulate([1, 2, 3, 4, 5])
    for v in list:
        print(v, end=' ')
    print()
    list = accumulate([1, 2, 3, 4, 5], initial=100)
    for v in list:
        print(v, end=' ')
    print()
    list = accumulate([1, 2, 3, 4, 5], mul)
    for v in list:
        print(v, end=' ')
    print()

if __name__ == '__main__':
    main()