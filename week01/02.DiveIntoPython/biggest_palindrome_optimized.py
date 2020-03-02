def is_palindrome(num):
    return str(num) == str(num)[::-1]


def to_number(lst):
    s = [str(x) for x in lst]
    s = ''.join(s)
    s = int(s)
    return s


def to_list(num):
    return [int(x) for x in str(num)]


def get_biggest_palindrome(num):
    if num <= 11:
        raise ValueError('There are no palindromes lower than 11.')

    if (is_palindrome(num)):
        num -= 1

    num_list = to_list(num)
    length = len(num_list)

    if num_list[0] == 1 and all(x == 0 for x in num_list[1:]):
        return num - 1

    pivot = []
    if length % 2 != 0:
        pivot = [num_list[length // 2]]

    left = num_list[:length // 2]
    right = num_list[(length // 2) + bool(pivot):]

    left_number = to_number(left)
    right_number = to_number(right)

    if (left_number < right_number):
        right = left[::-1]
    else:
        right = left[::-1]

        new = left + pivot + right

        if (to_number(new) > num):
            left_number -= 1

            if (pivot):
                pivot[0] -= 1
                if (pivot[0]) < 0:
                    pivot[0] = 9

            new_left = to_list(left_number)
            if len(new_left) < len(left):
                pivot = [9]

            left = new_left[:]
            right = left[::-1]

    return to_number(left + pivot + right)


print(get_biggest_palindrome(7550645))
