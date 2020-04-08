from abc import ABC, abstractmethod


def required(method):
    def required_method(instance, *args, **kwargs):
        method_name = method.__name__

        if method_name not in instance.__dict__:
            raise AttributeError(
                f'All classes that inherit from "{instance.__class__.__name__}" must provide "{method_name}" method.'
            )

        return method(instance, *args, **kwargs)

    return required_method


class Animal(ABC):
    @abstractmethod
    def eat(self, food):
        pass

    @required
    def sleep(self, time=10):
        pass


class Dog(Animal):
    pass


sharo = Dog()
# sharo.sleep()
