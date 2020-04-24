from datetime import datetime


my_datetime = datetime


def is_weekday():
    today = my_datetime.today()
    return (0 <= today.weekday() < 5)
