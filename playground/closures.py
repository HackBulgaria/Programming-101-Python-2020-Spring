# def make_multiple(n):
#     def multiply(x):
#         print(f'{x} * {n} is ', x * n)

#     return multiply


# times_three = make_multiple(3)
# times_five = make_multiple(5)

# del make_multiple

# times_three(10)  # == make_multiple(3)(10)

# print('Closure of make_multiple', make_multiple.__closure__)
# print('Closure of times_three', times_three.__closure__[0].cell_contents)
# print('Closure of times_five', times_five.__closure__)

# times_five(100)
# times_five(10)

# times_three(20)


def add_discount(promo=100):
    print('In function that returns decorator')

    def inner(func):
        print('In decorator')

        def discounted(user, money):
            print('closure for: ', func.__name__)
            return func(user, money * (promo / 100))  # return value is the return value of `func`
        return discounted  # return value is closure
    return inner  # return value is decorator


# decorator = add_discount(promo=20)
# print('after add_discount return value')
# pay_phone = decorator(pay_phone)


# @shano
@add_discount(promo=20)
def pay_phone(user, money):
    print('phone', user, money)


# @add_discount()
# def pay_net(user, money):
#     print('net', user, money)

print('Before pay_phone is called')
pay_phone('marto', 100)
# pay_net('marto', 100)
