import time
from contextlib import contextmanager, ContextDecorator


class FileManager:
    def __init__(self, filename, mode='r'):
        print('In __init__')
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print('Entering')
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('Exiting')
        self.file.close()


@contextmanager
def file_manager(filename, mode='r'):
    try:
        file = open(filename, mode)
        # ========================
        yield file
        # ========================
    except Exception:
        pass
    finally:
        file.close()


with FileManager('demo1.py', 'w') as f:
    f.write('print("Marto e bok")')

with file_manager('demo2.py', 'w') as f:
    f.write('print("Marto e bok")')


class stopwatch(ContextDecorator):
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        print('Finished in: ', time.time() - self.start)


@stopwatch()
def foo():
    time.sleep(1)

    with stopwatch():
        print('in with block')
        time.sleep(1)

    print('outside the with block')


foo()
