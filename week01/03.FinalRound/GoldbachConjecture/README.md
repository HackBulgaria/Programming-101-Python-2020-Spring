# Goldbach Conjecture

Implement a function, called `goldbach(n)` which returns a list of tuples, that is the goldbach conjecture for the given number `n`.

The Goldbach Conjecture states:

> Every even integer greater than 2 can be expressed as the sum of two primes.

Keep in mind that there can be more than one combination of two primes, that sums up to the given number.

**The result should be sorted by the first item in the tuple.**

For example:

- `4 = 2 + 2`
- `6 = 3 + 3`
- `8 = 3 + 5`
- `10 = 3 + 7 = 5 + 5`
- `100 = 3 + 97 = 11 + 89 = 17 + 83 = 29 + 71 = 41 + 59 = 47 + 53`

## Signature

```python
def goldbach(n):
    pass
```

## Test examples

```python
>>> goldbach(4)
[(2,2)]
>>> goldbach(6)
[(3,3)]
>>> goldbach(8)
[(3,5)]
>>> goldbach(10)
[(3,7), (5,5)]
>>> goldbach(100)
[(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]
```
