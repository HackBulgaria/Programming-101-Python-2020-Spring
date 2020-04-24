## Presentation

https://slides.com/hackbulgaria/python-101-9th-mocking/

## You should write tests for the following functions

### 1

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

### 2

Remember [Measure Performance task](https://github.com/HackBulgaria/Programming-101-Python-2020-Spring/tree/master/week07/01.ContextManagers#measure-performance)? Rework the tests to test if the context manager **prints the correct values**.

### 3

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

### 4

```
from random import randint

def big_possitive_pow():
    x = randint(100, 10000)
    y = randint(-10, 100)

    if y < 1:
        raise ValueError('Try again.')

    return x ** y
```

### 5

You don't need to install the libraries!

```
import requests
from bs4 import BeautifulSoup


def get_url_title(*, url):
    try:
        # Pretend to be a bot.
        headers = {'User-Agent': 'Testbot'}
        response = requests.get(url, headers=headers, timeout=10)
    except RequestException as request_exception:
        raise Exception(f'Couldn\'t request {url}. This was the exception {request_exception}')

    if not response.ok:
        raise Exception(f'Response for {url} was not ok.')

    soup = BeautifulSoup(response.content, 'html.parser')
    title_tag = soup.title

    if title_tag
      return title_tag.string

    return ''
```
