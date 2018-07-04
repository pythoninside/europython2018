class Meta(type):
    def __new__(meta, name, bases, dct):
        result = super().__new__(meta, name, bases, dct)
        print(f'Called: __new__({meta}, {name}, {bases}, {dct} -> {result}')
        return result

    def __init__(cls, name, bases, dct):
        result = super().__init__(name, bases, dct)
        print(f'Called: __init__({cls}, {name}, {bases}, {dct} -> {result}')
        return result


class Point(object, metaclass=Meta):
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
