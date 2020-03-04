from datetime import datetime, timedelta


def validate_conditions(conditions):
    pass


def ensure_conditions(conditions):
    # Ensure all condtions have hours
    return conditions


def group_conditions(conditions):
    # TODO
    return conditions


def get_current_condition(conditions, start, now):
    return conditions[0]


def get_cancellation_fee(price, percent):
    return price * (percent / 100)


def get_cancellation_policy(
    conditions,
    price,
    start,
    now
):
    assert start < now


def main():
    now = datetime.now()
    booking_start = now + timedelta(hours=10)
    price = 1000
    conditions = [
        {'hours': 24, 'percent': 10},
        {'hours': 12, 'percent': 50},
        {'hours': 6, 'percent': 80},
        {'percent': 100}
    ]

    result = get_cancellation_policy(
        conditions,
        price,
        booking_start,
        now
    )
    print(result)


if __name__ == '__main__':
    main()
