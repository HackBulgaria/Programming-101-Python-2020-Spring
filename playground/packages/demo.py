from random import shuffle

def func(x):
    print('You will not see me')

from foo import func as func_new_name

from foo import sys

print(sys.path)

# print('Namespace after imports: ')
# print(dir())
# print('==========================')

# func(10)
# func_new_name(10)

# panda = foo.Panda()
# print(panda)

# print('Mega constant: ', foo._MEGA_CONSTANT)
