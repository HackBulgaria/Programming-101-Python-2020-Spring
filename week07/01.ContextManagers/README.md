# Context Managers

**NOTE: All tasks should be implemented using a class context managers and @contextmanager generator!**

## Silence errors

Implement a context manager that silences specific exceptions. It can accept the message of the exception as non-required argument.

```python
with silence_exception(ValueError):
    # nothing should happen
    raise ValueError('Test')

with silence_exception(ValueError):
    # the error should be re-raised since it is not expected.
    raise TypeError('Test')

with silence_exception(ValueError, 'Test'):
    # nothing should happen
    raise ValueError('Test')

with silence_exception(ValueError, 'Testing.'):
    # the error should be re-raised since it is not expected.
    raise ValueError('Test')
```

## Change Decimal Precision

Implement a context manager that sets the precision of all Decimals in the with-block. Outside the block, the Decimals must be preserved with their default precision. _Think for raised exceptions!_

```python
with change_precision(2):
    print(Decimal('1.123132132') + Decimal('2.23232'))  # 3.4

print(Decimal('1.123132132') + Decimal('2.23232'))  # 3.355452132
```

Check this for help: https://docs.python.org/3/library/decimal.html#quick-start-tutorial

## Measure Performance

Implement a context manager that tracks the performance of a code block using "benchmarks". The context manager should print how much time each code block took. When the with-block is finished, the context manager should print how much time the whole block took.

The benchmarks can accept a string message so it's easier to know what is measured. If there is no message passed - use the index of the benchmark as shown below.

Each benchmark can optionally restart the context manager time (show below).

```python
with measure_performance() as p:
    time.sleep(1)
    p.benchmark('1st step')

    time.sleep(2)
    p.benchmark('2nd step', restart=True)

    time.sleep(3)
    p.benchmark()
```

The output is:

```
1st step: 1.0011475086212158
2nd step: 3.0017237663269043
Benchmark No.3: 3.003134250640869
Finished for:  6.0052361488342285
```

**NOTE: All tasks should be implemented using a class context managers and @contextmanager generator!**
