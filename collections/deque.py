#!/usr/bin/env python

from collections import deque

def print_deque(d):
    for elem in d:  # iterate
        print(elem.upper(), end=" ")
    print()

def main():
    d = deque('ghi')
    print_deque(d)
    
    d.append('j')
    d.appendleft('f')
    print_deque(d)

    print(d.pop())
    print(d.popleft())
    print_deque(d)

    print(list(d))
    print(d[0])
    print(d[-1])

    print(list(reversed(d)))
    print('h' in d)
    d.extend('jkl')
    print_deque(d)
    d.extendleft('def')
    print_deque(d)

    d.rotate(1)  # deque の要素を全体で1ステップだけ右にローテート
    print_deque(d)
    d.rotate(-1) # 元に戻す
    print_deque(d)

    rd = deque(reversed(d))
    print_deque(rd)

    d.clear()
    try:
        d.pop()
    except IndexError as e:
        print(e)
    
    

if __name__ == '__main__':
    main()