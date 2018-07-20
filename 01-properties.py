from math import pi


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        assert isinstance(value, int), 'Booooo! Expecting an int'
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        assert isinstance(value, int), 'Booooo! Expecting an int'
        self._y = value

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f'A Point at {self.x}, {self.y}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, value):
        assert isinstance(value, Point), 'Booooo! Expecting a Point'
        self._center = value

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        assert isinstance(value, int), 'Booooo! Expecting an int'
        self._radius = value

    @property
    def area(self):
        return pi * self.radius ** 2

    def __str__(self):
        return f'A Circle at {self.center.x}, {self.center.y} and ' + \
               f'radius {self.radius}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.center!r}, {self.radius!r})'
