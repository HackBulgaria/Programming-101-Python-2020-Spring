# def fib():
#     print('Initializing generator')
#     a, b = 1, 1

#     while a < 100:
#         print('Current: ', a)
#         yield a
#         a, b = b, a + b


# fib_generator = fib()

# next(fib_generator)
# next(fib_generator)
# next(fib_generator)
# next(fib_generator)

# print('=========')

# new_fib_generator = fib_generator

# for _ in new_fib_generator:
#     pass

# print('=========')

# for _ in fib_generator:
#     pass


def complex_generator():
    items = [1, 2, 3, 4, 5, 6, 7, 8]
    wtf = 1

    for item in items:
        print('Yielding: ', item)
        value = yield item

        # return 'Opa.'

        if (item == 8):
            print('No more ...')
            print(f'Last value is {value}')

        # value is None when the `next` is used a.k.a the first time the generator is triggered for sure.
        if value is not None:
            wtf += item + value

        print(wtf)

    return 'The end of the complex_generator'


gen = complex_generator()

next(gen)
next(gen)

gen.send(10)  # Sends 10 to the generator and restarts it. Cannot be used if the generator is not started!!!
gen.send(100)

# gen.close()  Will close the generator and the next time you try to use the generator

# for i in range(4):
for i in range(5):
    gen.send(i)
