import sys

__all__ = ['func']

print('namespace in foo: ', dir())

def func(x):
    print(f'Passed arg: {x}')


class Panda:
    pass

_MEGA_CONSTANT = 42
