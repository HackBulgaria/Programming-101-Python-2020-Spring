## Presentation

https://slides.com/hackbulgaria/python-101-9th-mocking/

## You should write tests for the following functions

### 1

```
from random import randint

def big_possitive_pow():
    x = randint(100, 10000)
    y = randint(-10, 100)

    if y < 1:
        raise ValueError('Try again.')

    return x ** y
```

### 2

```
from datetime import datetime

def get_booking_status(booking):
    now = datetime.now()

    if booking.cancelled:
        return 'Cancelled'

    if booking.is_fully_paid():
        return 'Paid'

    if now < booking.start:
        return 'Upcoming'

    return 'Waiting taxes'
```

### 3

Remember the [Cancellation policy task](https://github.com/HackBulgaria/Programming-101-Python-2020-Spring/tree/master/week02/02.CancellationPolicy)? Rework the solution and the tests and stop expecting `now` as argument!

```
def get_cancellation_policy(conditions, price, start):
    now = datetime.now()

    assert now < start, 'Invalid booking start.'
    validate_conditions(conditions)

    ensured_conditions = ensure_conditions(conditions)

    if (len(ensured_conditions)) == 1:
        return get_cancellation_fee(price, ensured_conditions[0]['percent'])

    sorted_conditions = sort_conditions(ensured_conditions)
    paired_conditions = pair_conditions(sorted_conditions)

    current = get_current_condition(paired_conditions, start, now)

    return get_cancellation_fee(price, current)
```

### 4

Remember [Measure Performance task](https://github.com/HackBulgaria/Programming-101-Python-2020-Spring/tree/master/week07/01.ContextManagers#measure-performance)? Rework the tests to test if the context manager **prints the correct values**.