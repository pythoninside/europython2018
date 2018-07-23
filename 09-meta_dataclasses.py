from dataclasses import dataclass
from math import pi
import typing


class TypeChecker:
    required_type = object

    def __init__(self, name=None):
        self.name = f'_{name}'

    def __get__(self, instance, owner=None):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        assert isinstance(value, self.required_type), \
               f'Booooo! Expecting a {self.required_type.__name__}'
        instance.__dict__[self.name] = value


def typed_dataclass(cls):
    cls = dataclass(cls)

    for var_name, var_type in typing.get_type_hints(cls).items():
        class Checker(TypeChecker):
            required_type = var_type

        setattr(cls, var_name, Checker(var_name))
    return cls


class TypeCheckMeta(type):
    def __new__(meta, name, bases, dct):
        cls = super().__new__(meta, name, bases, dct)
        return typed_dataclass(cls)


class Base(metaclass=TypeCheckMeta):
    pass


class Point(Base):
    x: int
    y: int

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f'A Point at {self.x}, {self.y}'


class Circle(Base):
    center: Point
    radius: int

    @property
    def area(self):
        return pi * self.radius ** 2

    def __str__(self):
        return f'A Circle at {self.center.x}, {self.center.y} and ' + \
               f'radius {self.radius}'
