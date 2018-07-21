import ast


CODE = """
import sys

print('Hello world')
"""


class StrUpper(ast.NodeTransformer):
    def visit_Str(self, node):
        # Replace each string with a call to <string>.upper()
        new_node = ast.Call(
            func=ast.Attribute(value=node, attr='upper', ctx=ast.Load()),
            args=[],
            keywords=[])
        return new_node


tree = ast.parse(CODE)
print('---')
print(ast.dump(tree))
print('---')
exec(compile(tree, filename='', mode='exec'))

tree = StrUpper().visit(tree)
ast.fix_missing_locations(tree)
print('---')
print(ast.dump(tree))
print('---')
exec(compile(tree, filename='', mode='exec'))
