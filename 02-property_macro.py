from math import pi


def check_type(name, required_type):
    variable_name = f'_{name}'

    @property
    def variable(self):
        return getattr(self, variable_name)

    @variable.setter
    def variable(self, value):
        assert isinstance(value, required_type), \
               f'Booooo! Expecting a {required_type.__name__}'
        setattr(self, variable_name, value)
    return variable


class Point:
    x = check_type('x', int)
    y = check_type('y', int)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f'A Point at {self.x}, {self.y}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'


class Circle:
    center = check_type('center', Point)
    radius = check_type('radius', int)

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    @property
    def area(self):
        return pi * self.radius ** 2

    def __str__(self):
        return f'A Circle at {self.center.x}, {self.center.y} and ' + \
               f'radius {self.radius}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.center!r}, {self.radius!r})'
