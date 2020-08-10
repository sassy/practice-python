#!/usr/bin/env python

from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def sound(self):
        pass


class Cat(Animal):
    def sound(self):
        print("Meow")

class Dog():
    def sound(self):
        print("Bow")

Animal.register(Dog)


if __name__ == "__main__":
    assert issubclass(Cat().__class__, Animal)
    assert isinstance(Cat(), Animal)
    assert issubclass(Dog().__class__, Animal)
    assert isinstance(Dog(), Animal)
    Cat().sound()
    Dog().sound()