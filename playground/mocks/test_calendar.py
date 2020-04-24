import unittest
from unittest.mock import patch
from datetime import datetime

from calendar import is_weekday


class CalendarTests(unittest.TestCase):
    @patch('calendar.my_datetime', autospec=True)
    def test_sunday_is_not_weekday(self, datetime_mock):
        sunday = datetime(year=2020, month=4, day=26)
        datetime_mock.today.return_value = sunday

        self.assertFalse(is_weekday())


if __name__ == '__main__':
    unittest.main()
