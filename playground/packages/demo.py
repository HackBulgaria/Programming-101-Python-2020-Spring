print('Namespace before imports: ')
print(dir())
print('==========================')

import sys
from random import shuffle

import foo

print('Namespace after imports: ')
print(dir())
print('==========================')

print(sys.path)

foo.func(10)

panda = foo.Panda()
print(panda)
