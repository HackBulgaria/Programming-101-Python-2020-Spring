# Python Problems

-   [Sum of all digits of a number](#sum-of-all-digits-of-a-number)
    -   [Signature ](#signature-)
    -   [Test examples](#test-examples)
-   [Turn a number into a list of digits](#turn-a-number-into-a-list-of-digits)
    -   [Signature ](#signature--1)
    -   [Test examples](#test-examples-1)
-   [Turn a list of digits into a number](#turn-a-list-of-digits-into-a-number)
    -   [Signature ](#signature--2)
    -   [Test examples](#test-examples-2)
-   [Factorial Digits](#factorial-digits)
    -   [Signature ](#signature--3)
    -   [Test examples](#test-examples-3)
-   [Palindrome](#palindrome)
    -   [Signature ](#signature--4)
    -   [Test examples](#test-examples-4)
-   [Vowels in a string](#vowels-in-a-string)
    -   [Signature ](#signature--5)
    -   [Test examples](#test-examples-5)
-   [Consonants in a string](#consonants-in-a-string)
    -   [Signature ](#signature--6)
    -   [Test examples](#test-examples-6)
-   [Char Histogram](#char-histogram)
    -   [Signature ](#signature--7)
    -   [Test examples](#test-examples-7)
-   [Sum Numbers in Matrix](#sum-numbers-in-matrix)
    -   [Examples:](#examples)
-   [NaN Expand](#nan-expand)
    -   [Examples](#examples-1)
-   [Integer prime factorization](#integer-prime-factorization)
    -   [Signature](#signature)
    -   [Test examples](#test-examples-8)
-   [The group function](#the-group-function)
-   [Longest subsequence of equal consecutive elements](#longest-subsequence-of-equal-consecutive-elements)
    -   [Signature](#signature-1)
    -   [Test examples](#test-examples-9)
-   [Word counter](#word-counter)
    -   [For example:](#for-example)
    -   [Example inputs:](#example-inputs)

In a file called `week1_solutions.py`, solve the following problems:

## Sum of all digits of a number

Given an integer, implement a function, called `sum_of_digits(n)` that calculates the sum of n's digits.

If a negative number is given, our function should work as if it was positive.

Keep in mind that in Python, there is a special operator for integer division!

```python
>>> 5 / 2
2.5
>>> 5 // 2
2
```

### Signature

```python
def sum_of_digits(n):
    pass
```

### Test examples

```python
>>> sum_of_digits(1325132435356)
43
>>> sum_of_digits(123)
6
>>> sum_of_digits(6)
6
>>> sum_of_digits(-10)
1
```

## Turn a number into a list of digits

Implement a function, called `to_digits(n)`, which takes an integer `n` and returns a list, containing the digits of `n`.

### Signature

```python
def to_digits(n):
    pass
```

### Test examples

```python
>>> to_digits(123)
[1, 2, 3]
>>> to_digits(99999)
[9, 9, 9, 9, 9]
>>> to_digits(123023)
[1, 2, 3, 0, 2, 3]
```

## Turn a list of digits into a number

Implement a function, called to_number(digits), which takes a list of integers - digits and returns the number, containing those digits.

### Signature

```python
def to_number(digits):
    pass
```

### Test examples

```python
>>> to_number([1,2,3])
123
>>> to_number([9,9,9,9,9])
99999
>>> to_number([1,2,3,0,2,3])
123023
>>> to_number([21, 2, 33])
21233
```

## Factorial Digits

Implement a function `fact_digits(n)`, that takes an integer and returns the sum of the factorials of each digit of `n`.

For example, if n = 145, we want 1! + 4! + 5!

### Signature

```python
def fact_digits(n):
    pass
```

### Test examples

```python
>>> fact_digits(111)
3
>>> fact_digits(145)
145
>>> fact_digits(999)
1088640
```

## Palindrome

Implement a function, called `palindrome(obj)`, which takes an object (could be anything) and checks if it's string representation is a palindrome.

For example, the integer `121` and the string `"kapak"` are palindromes. The function should work with both..

**Hint - check Python's [str()](https://docs.python.org/3/library/stdtypes.html#str) function**

### Signature

```python
def palindrome(n):
    pass
```

### Test examples

```python
>>> palindrome(121)
True
>>> palindrome("kapak")
True
>>> palindrome("baba")
False
```

## Vowels in a string

Implement a function, called `count_vowels(str)`, which returns the count of all vowels in the string `str`.

**Count uppercase vowels aswell!**

The English vowels are `aeiouy`.

### Signature

```python
def count_vowels(str):
    pass
```

### Test examples

```python
>>> count_vowels("Python")
2
>>> count_vowels("Theistareykjarbunga") #It's a volcano name!
8
>>> count_vowels("grrrrgh!")
0
>>> count_vowels("Github is the second best thing that happend to programmers, after the keyboard!")
22
>>> count_vowels("A nice day to code!")
8
```

## Consonants in a string

Implement a function, called `count_consonants(str)`, which returns the count of all consonants in the string `str`.

**Count uppercase consonants as well!**

The English consonants are `bcdfghjklmnpqrstvwxz`.

### Signature

```python
def count_consonants(str):
    pass
```

### Test examples

```python
>>> count_consonants("Python")
4
>>> count_consonants("Theistareykjarbunga") #It's a volcano name!
11
>>> count_consonants("grrrrgh!")
7
>>> count_consonants("Github is the second best thing that happend to programmers, after the keyboard!")
44
>>> count_consonants("A nice day to code!")
6
```

## Char Histogram

Implement a funcion, called `char_histogram(string)`, which takes a string and returns a dictionary, where each key is a character from `string` and its value is the number of occurrences of that char in `string`.

### Signature

```python
def char_histogram(string):
    pass
```

### Test examples

```python
>> char_histogram("Python!")
{ 'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1 }
>>> char_histogram("AAAAaaa!!!")
{ 'A': 4, 'a': 3, '!": 3 }
```

## Sum Numbers in Matrix

You are given a `NxM` matrix of integer numbers.

Implement a function, called `sum_matrix(m)` that returns the sum of all numbers in the matrix.

The matrix will be represented as nested lists in Python.

### Examples:

```python
>>> m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> sum_matrix(m)
45
>>> m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> sum_matrix(m)
0
>>> m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
>>> sum_matrix(m)
55
```

## NaN Expand

In most programming languages, `NaN` stands for `Not a Number`.

If we take a look at the following JavaScript code:

```javascript
typeof NaN === 'number'; // true
```

We will see that in JavaScript, `NaN` stands for `Not a NaN`, which is recursive by nature.

Implement a Python function, called `nan_expand(times)`, which returns the expansion of `NaN` (In JavaScript terms :P) that many `times`.

For example:

-   If we expand `NaN` once (`times=1`), we will have `"Not a NaN"`
-   If we expand `NaN` twice (`times=2`), we will have `"Not a Not a NaN"`
-   If `times=3`, we have `"Not a Not a Not a NaN"`
-   And so on ...

### Examples

```python
>>> nan_expand(0)
""
>>> nan_expand(1)
"Not a NaN"
>>> nan_expand(2)
"Not a Not a NaN"
>>> nan_expand(3)
"Not a Not a Not a NaN"
```

## Integer prime factorization

Given an integer `n`, we can factor it in the following form:

```
n = p1^a1 * p2^a2 * ... * pn^an
```

Where each `p` is a prime number and each `a` is an integer and `p^a` means `p` to the power of `a`.

[This is called prime factorization.](http://mathworld.wolfram.com/PrimeFactorization.html)

Lets see few examples:

```
10 = 2^1 * 5^1
25 = 5^2
356 = 2^2 * 89 ^ 1
```

Implement a function, called `prime_factorization(n)`, which takes an integer and returns a list of tuples `(pi, ai)` that is the result of the factorization.

The list should be sorted in increasing order of the prime numbers.

### Signature

```python
def prime_factorization(n):
    pass
```

### Test examples

```python
>>> prime_factorization(10)
[(2, 1), (5, 1)] # This is 2^1 * 5^1
>>> prime_factorization(14)
[(2, 1), (7, 1)]
>>> prime_factorization(356)
[(2, 2), (89, 1)]
>>> prime_factorization(89)
[(89, 1)] # 89 is a prime number
>>> prime_factorization(1000)
[(2, 3), (5, 3)]
```

## The group function

We are going to implement a very helpful function, called `group`.

`group` takes a list of things and returns a list of group, where each group is formed by all **equal consecutive elements** in the list.

For example:

```python
group([1, 1, 1, 2, 3, 1, 1]) == [[1, 1, 1], [2], [3], [1, 1]]
group([1, 2, 1, 2, 3, 3]) == [[1], [2], [1], [2], [3, 3]]
```

## Longest subsequence of equal consecutive elements

Implement the function `max_consecutive(items)`, which takes a list of things and returns an integer - the count of elements in the longest subsequence of equal consecutive elements.

For example, in the list `[1, 2, 3, 3, 3, 3, 4, 3, 3]`, the result is 4, where the longest subsequence is formed by `3, 3, 3, 3`

### Signature

```python
def max_consecutive(items):
    pass
```

### Test examples

```python
>>> max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3])
4
>>> max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5])
3
```

## Word counter

You are given a rectangular table filled with characters and a `word`.
Your task is to count the occurences of a `word` in the table. The word can be found horizontaly, vertically and across both left to right and right to left.

### For example:

Find the word `ivan` in the table:

| i   | v   | a   | n   |
| --- | --- | --- | --- |
| e   | _v_ | _n_ | h   |
| i   | n   | _a_ | v   |
| m   | v   | _v_ | _n_ |
| q   | r   | _i_ | t   |

Result:

```
3
```

The first thing you need to do is to input the word you are looking for.
You need to provide the number of rows and columns of your table.
Then input the characters into the table.

Note: If the word you are looking for is longer than the length of your rows, columns or diagonals, you need to return message to the user that the input was invalid.

### Example inputs:

#### Example 1:

```
ivan
5 4
i v a n
e v n h
i n a v
m v v n
q r i t
```

Should print:

```
3
```

#### Example 2:

```
actually
8 15
i v a n q h r e z g t z o y m
e v n h t r x e k y d a i l c
i a c t u a l l y m c x r l e
m v c n p u a m n t l u e a a
q r i t w e a q u p r x t u z
p e a c t u a l l y w p y t m
o y h t r e l u f p q n z c s
p a c t u a l l y u r e q a r
```

Should print:

```
4
```

#### Example 3:

```
madam
8 12
z v a n q h r e z g t z
e v m h t r x e k y m a
i a c a u a l l y a c x
m v c n d u a m d t l u
q t i t w a a a u p r x
p e m a d a m l l y w p
o y h t e e l u f p q n
p a c t u a l l y u r e
```

Should print:

```
3
```

Notice that this should print 3, not 6!

#### Example 4:

```
table
3 4
```

Should print:

```
Invalid number of rows or columns!
```
