import sys
from random import shuffle

from foo import *

print('Namespace after imports: ')
print(dir())
print('==========================')

func(10)

panda = foo.Panda()
print(panda)

print('Mega constant: ', foo._MEGA_CONSTANT)
