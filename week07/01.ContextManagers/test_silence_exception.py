import unittest

from silence_exception import silence_exception, SilenceException


class SilenceExceptionTests(unittest.TestCase):
    def test_silences_passed_exception(self):
        exception = None

        try:
            with silence_exception(ValueError):
                raise ValueError('Testing.')
        except Exception as exc:
            exception = exc

        self.assertIsNone(exception)

    def test_not_silences_different_exception_from_passed_one(self):
        with self.assertRaises(ValueError):
            with silence_exception(TypeError):
                raise ValueError('Testing.')

    def test_not_silences_passed_exception_outside_context_manager(self):
        with self.assertRaises(ValueError, msg='Testing outside with-block'):
            with silence_exception(ValueError):
                raise ValueError('Testing inside with-block')

            raise ValueError('Testing outside with-block')

    def test_silences_passed_exception_with_correct_message(self):
        exception = None
        exc_message = 'Testing with msg argument.'

        try:
            with silence_exception(ValueError, msg=exc_message):
                raise ValueError(exc_message)
        except Exception as exc:
            exception = exc

        self.assertIsNone(exception)

    def test_not_silences_passed_exception_with_different_message(self):
        exc_message = 'Testing with msg argument.'

        with self.assertRaises(ValueError):
            with silence_exception(ValueError, msg=exc_message):
                raise ValueError(f'{exc_message} - different.')

    def test_not_silences_different_exception_with_same_message(self):
        exc_message = 'Testing with msg argument.'

        with self.assertRaises(TypeError):
            with silence_exception(ValueError, msg=exc_message):
                raise TypeError(exc_message)


class SilenceExceptionClassTests(unittest.TestCase):
    def test_silences_passed_exception(self):
        exception = None

        try:
            with SilenceException(ValueError):
                raise ValueError('Testing.')
        except Exception as exc:
            exception = exc

        self.assertIsNone(exception)

    def test_not_silences_different_exception_from_passed_one(self):
        with self.assertRaises(ValueError):
            with SilenceException(TypeError):
                raise ValueError('Testing.')

    def test_not_silences_passed_exception_outside_context_manager(self):
        with self.assertRaises(ValueError, msg='Testing outside with-block'):
            with SilenceException(ValueError):
                raise ValueError('Testing inside with-block')

            raise ValueError('Testing outside with-block')

    def test_silences_passed_exception_with_correct_message(self):
        exception = None
        exc_message = 'Testing with msg argument.'

        try:
            with SilenceException(ValueError, msg=exc_message):
                raise ValueError(exc_message)
        except Exception as exc:
            exception = exc

        self.assertIsNone(exception)

    def test_not_silences_passed_exception_with_different_message(self):
        exc_message = 'Testing with msg argument.'

        with self.assertRaises(ValueError):
            with SilenceException(ValueError, msg=exc_message):
                raise ValueError(f'{exc_message} - different.')

    def test_not_silences_different_exception_with_same_message(self):
        exc_message = 'Testing with msg argument.'

        with self.assertRaises(TypeError):
            with SilenceException(ValueError, msg=exc_message):
                raise TypeError(exc_message)


if __name__ == '__main__':
    unittest.main()
