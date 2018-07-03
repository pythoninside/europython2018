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


ensure_int = lambda name: check_type(name, int)             # noqa
ensure_point = lambda name: check_type(name, Point)         # noqa


class Point:
    x = ensure_int('x')
    y = ensure_int('y')

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
    center = ensure_point('center')
    radius = ensure_int('radius')

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


# Fewer lines of code!
# Mind-bending?
