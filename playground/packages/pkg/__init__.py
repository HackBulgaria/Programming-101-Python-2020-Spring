print('In pkg init...')

import pkg.foo1
print('foo1: ', foo1)


from . import foo1
print('foo1: ', foo1)


from pkg import foo1
print('foo1: ', foo1)


# from pkg import foo3
