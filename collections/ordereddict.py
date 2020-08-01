#!/usr/bin/env python

from collections import OrderedDict

def main():
    d = OrderedDict.fromkeys('abcde')
    print(''.join(d.keys()))
    d.move_to_end('b')
    print(''.join(d.keys()))
    d.move_to_end('b', last=False)
    print(''.join(d.keys()))

    d2 = OrderedDict()
    d2['a'] = 1
    d2['b'] = 2
    d2['c'] = 3
    print(''.join(d2.keys()))
    print(d2.values())
    d2.move_to_end('b')
    print(''.join(d2.keys()))

if __name__ == '__main__':
    main()