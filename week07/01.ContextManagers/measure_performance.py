import os
import time


class MeasurePerformance:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self._benchmarks = []

    def __enter__(self):
        self.file = open(self.filename, 'w')

        self.original_start = time.time()
        self.start = self.original_start

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            if exc_type:
                self.file.close()
                os.remove(self.filename)
            else:
                self.file.write('\n'.join(self._benchmarks))
                self.file.write(f'\nFinished for: {int(time.time() - self.original_start)}s')
                self.file.close()

    def get_exceeded_time(self):
        return int(time.time() - self.start)

    def benchmark(self, msg=None, restart=False):
        exceeded_time = self.get_exceeded_time()

        if restart:
            self.start = time.time()

        if msg is None:
            msg = f'Benchmark No.{len(self._benchmarks) + 1}'

        benchmark = f'{msg}: {exceeded_time}s'
        self._benchmarks.append(benchmark)
