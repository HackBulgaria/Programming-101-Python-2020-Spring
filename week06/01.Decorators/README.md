## @accepts

Make a decorator `@accepts` that takes as many arguments as the function takes. That decorator specify the types of the arguments that your function takes. If any of the arguments does not match the type in the decorator raise a `TypeError`

### Examples

```python
@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

say_hello(4)

TypeError: Argument "name" of say_hello is not str!
```

```python
@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))

deposit("Marto", 10)
```

Note that this is just a nice example. In real life you don't want use this!

## @performance(file_name)

Make a decorator `@performance` that takes a `file_name` and writes in to this file a log. New line for every call of the decorated function. This decorator should log the time needed for the decorated function to execute.

### Example

```python
@performance('log.txt')
def something_heavy():
    sleep(2)
    return "I am done!"

something_heavy()

I am done!
```

And the log file should look like this:

```
get_low was called and took 2.00 seconds to complete
get_low was called and took 2.10 seconds to complete
```

## @required

Make a decorator `@required` that makes all decorated methods with throw exception if they are not overrided in the child classes.

### Example

```python
class Animal:
    @required
    def eat(self, food):
        pass


class Panda(Animal):
    pass

p = Panda()
p.eat('bamboo')

Exception: All classes that inherit from "Animal" must provide "eat" method.
```

## @silence(file_name)

Make a decorator `@silence` that accepts a `file_name` as an argument. All functions that are decorated with it should always run successfully. If an error is raised, it should be logged in the given file.

```python
@silence('errors.txt')
def foo(x)
    if x > 50:
        raise ValueError('Omg.')

foo(10)
foo(100)

# in errors.txt
Calling `foo` raised an error - ValueError: 'Omg.'. Provided arguments: (100, ).
```
