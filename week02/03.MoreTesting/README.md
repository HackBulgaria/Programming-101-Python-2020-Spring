## Python sort

Implement a function, called `my_sort` that takes 3 arguments. The arguments are:

- `iterable` - list or tuple that has to be sorted. Preserve the type in the return value. **Must have default value**
- `ascending` - boolean that controls the sorting order. **Must have default value**
- `key` - string that serves as a lookup key if the `iterable` argument is a list of dictionaries. **Must have default value**

The function should return the given iterable sorted in order that is controlled by the `ascending` value.

**NOTE: You should NOT use Python's builtin list.sort() or sorted()**

### Test examples

```
>>> my_sort([])
[]
>>> my_sort((10,8,9,10,100))
(8, 9, 10, 10, 100)
>>> my_sort([10, 8, 9, 10, 100], False)
[100, 10, 10, 9, 8]
>>> my_sort(iterable=[{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}], key='age')
[{'name': 'Marto', 'age': 24}, {'name': 'Sashko', 'age': 25}, {'name': 'Ivo', 'age': 27}]
```

## Simplify fractions

Implement a function, called `simplify_fraction(fraction)` that takes a tuple of the form `(nominator, denominator)` and simplifies the fraction.

The function should return the fraction in it's irreducible form.

For example, a fraction `3/9` can be reduced by dividing both the nominator and the denominator by 3. We end up with `1/3` which is irreducible.

### Test examples

```
>>> simplify_fraction((3,9))
(1,3)
>>> simplify_fraction((1,7))
(1,7)
>>> simplify_fraction((4,10))
(2,5)
>>> simplify_fraction((462,63))
(3,22)
```

## Collect fractions

Implement a function, called `collect_fractions(fractions)` where `fractions` is a list of tuples of the form `(nominator, denominator)`.

Both the nominator and the denominator are integers.
The function should return the sum of the fractions.

### Test examples

```
>>> collect_fractions([(1, 4), (1, 2)])
(3, 4)
>>> collect_fractions([(1, 7), (2, 6)])
(10,21)
```

## Sort array of fractions

Implement a function, called `sort_fractions(fractions, ascending = True)` where `fractions` is a list of tuples of the form `(nominator, denominator)` and `ascending` is boolean that controls the sorting direction.

Both the nominator and the denominator are integers.

The function should return the list, sorted depending on the `ascending` value.

### Test examples

```
>>> sort_fractions([(2, 3), (1, 2)])
[(1, 2), (2, 3)]
>>> sort_fractions([(2, 3), (1, 2), (1, 3)])
[(1, 3), (1, 2), (2, 3)]
>>> sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)])
[(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]
```
