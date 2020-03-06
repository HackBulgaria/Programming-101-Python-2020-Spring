from datetime import datetime, timedelta


def validate_conditions(conditions):
    counter = 0

    for condition in conditions:
        if not condition.get('hours'):
            counter += 1
        if condition.get('hours', 0) > 24:
            raise ValueError('Hours cannot be > 24.')

    if counter != 1:
        raise ValueError('Invalid conditions.')


def ensure_conditions(conditions):
    for condition in conditions:
        if 'hours' not in condition.keys():
            condition['hours'] = 0

    return conditions


def pair_conditions(conditions):
    result = []

    for index in range(len(conditions) - 1):
        left = conditions[index]
        right = conditions[index + 1]

        result.append((left, right))

    return result


def get_current_condition(pairs, start, now):
    for pair in pairs:
        lower_condition, higher_condition = pair

        lower_date = start - timedelta(hours=lower_condition['hours'])
        upper_date = start - timedelta(hours=higher_condition['hours'])

        if (now >= lower_date and now < upper_date):
            return higher_condition['percent']

    return pairs[0][0]['percent']


def get_cancellation_fee(price, percent):
    return price * (percent / 100)


def sort_conditions(conditions):
    return sorted(conditions, key=lambda c: c['hours'], reverse=True)


def get_cancellation_policy(
    conditions,
    price,
    start,
    now
):
    assert now < start, 'Invalid booking start.'
    validate_conditions(conditions)

    ensured_conditions = ensure_conditions(conditions)

    if (len(ensured_conditions)) == 1:
        return get_cancellation_fee(price, ensured_conditions[0]['percent'])

    sorted_conditions = sort_conditions(ensured_conditions)
    paired_conditions = pair_conditions(sorted_conditions)

    current = get_current_condition(paired_conditions, start, now)

    return get_cancellation_fee(price, current)


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
