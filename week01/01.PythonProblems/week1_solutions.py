def sum_of_digits(n):
    result = 0

    if n < 0:
        n = -1 * n

    while n > 0:
        result += n % 10
        n = n // 10

    return result


def sum2_of_digits(n):
    n_str = str(n)
    if n_str[0] == '-':
        n_str = n_str[1::]

    return sum([int(i) for i in n_str])


def to_digits(digits):
    return list(map(int, list(str(digits))))


def to_digits2(digits):
    return [int(i) for i in str(digits)]


def to_number(digits):
    number_str = "".join([str(d) for d in digits])
    return int(number_str)


# print(sum_of_digits(1325132435356))
# print(sum2_of_digits(1325132435356))

# print(to_digits(123))
# print(to_digits2(123))

print(to_number([21, 2, 33]))
