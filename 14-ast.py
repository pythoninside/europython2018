import ast

# This could come from a variety of sources: not just text. For instance, we
# could use inspect.get_source()
CODE = """
from dataclasses import dataclass


class TypeChecker:
    required_type = object

    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner=None):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        assert isinstance(value, self.required_type), \
               f'Booooo! Expecting a {self.required_type.__name__}'
        instance.__dict__[self.name] = value


def typed(cls):
    for var_name, var_type in cls.__annotations__.items():
        class Checker(TypeChecker):
            required_type = var_type
        setattr(cls, var_name, Checker(var_name))
    return cls


@dataclass
class Point:
    x: int
    y: int


p = Point(1, 2)
print(p)
p.x = 'foo'
print(p)
"""


class DecorateClasses(ast.NodeTransformer):
    def visit_ClassDef(self, node):
        if not [True for dec in node.decorator_list if dec.id == 'dataclass']:
            # Not a dataclass
            return node
        dec = ast.Name(id='typed', ctx=ast.Load())
        node.decorator_list.insert(0, dec)
        return node


tree = ast.parse(CODE)
exec(compile(tree, filename='', mode='exec'))

print('---')
tree = DecorateClasses().visit(tree)
ast.fix_missing_locations(tree)
exec(compile(tree, filename='', mode='exec'))
