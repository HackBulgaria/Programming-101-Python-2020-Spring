# Week 01 - Introduction to course & Python

[Intro slides](https://slides.com/hackbulgaria/python101-9th-opening)

## Data Structures

Here are the basic data structures, which will help you to solve our problems. Test them in the **REPL**.

All of the information you need can be found in the [docs](https://docs.python.org/3.8/tutorial/datastructures.html#data-structures)!

### List

It does not work like a traditional array. It is **heterogeneous**! This means it can store elements with different types in one list.

```python
things = [1 , 2, 'Ivo', [8, 'Rado']]
```

We can iterate:

```python
for thing in things:
    print(thing)
```

This outputs:

```
1
2
Ivo
[8, 'Rado']
```

### Dictionaries

Dictionaries are also known as hash tables / associative arrays.

They are used for key-value mapping.

**That's one of the most used & powerful data structures in Python.**

```python
youtube_views = {
    'Gangnam Style': 2096709806,
    'Baby': 1091538504,
    'Waka Waka': 746709408,
}

print(youtube_views['Waka Waka'])  # 746709408
```

Values are added by assigning them to `keys`.

```python
youtube_views['Wrecking Ball'] = 709604432
```

If that `key` already exists, the value held by that key will be replaced.

```python
youtube_views['Wrecking Ball'] = 85

print(youtube_views)
# {'Wrecking Ball': 85, 'Gangnam Style': 2096709806, 'Waka Waka': 746709408, 'Baby': 1091538504}
```

### Set

A set is an unordered collection with no duplicate elements.

Basic usage includes membership testing and eliminating duplicate entries.

Set objects also support mathematical operations like `union`, `intersection`, `difference`, and `symmetric difference`.

```python
sports = set()
sports.add('volleyball')
sports.add('football')
sports.add('basketball')

print('volleyball' in sports)  # True
print('tenis' in sports)  # False
```

Sets are perfect for searching elements with `in` since they can find them in constant time, in comparison to `O(n)` for `lists`.

### Tuple

Tuple are fixed-sized lists, which are **immutable**.

```python
super_heroes = ('Hackman', 'Spiderman', 'Hulk')

super_heroes[1] = 'Spindi'
```

This will result in the following error:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

### List Comprehension

Python has a nice syntax for list / dict & set operations, called "comprehensions".

For example, if we have the following cycle:

```python
numbers = []

for x in range(4, 10):
    numbers.append(x)
```

We can rewrite this as follows:

```python
numbers = [x for x in range(4, 10)]
```

We can also make different operations with the element, we append in list:

```python
squares = [x**2 for x in range(10)]
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
