#!/usr/bin/env python

from collections import namedtuple

def main():
    Car = namedtuple('Car', 'color mileage')
    my_car = Car('red', 3812.4)
    print(my_car.color)
    print(my_car.mileage)
    print(*my_car)


if __name__ == '__main__':
    main()