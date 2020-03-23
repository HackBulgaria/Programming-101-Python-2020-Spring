import unittest
import json

from mixins import Jsonable, WithSetAttributes, WithEqualAttributes


class Panda(Jsonable, WithSetAttributes, WithEqualAttributes):
    pass


class Car(Jsonable, WithSetAttributes, WithEqualAttributes):
    pass


class TestJsonable(unittest.TestCase):
    def test_to_json_returns_empty_json_for_objects_with_no_arguments(self):
        panda = Panda()

        result = panda.to_json(indent=4)
        expexted = {
            'type': Panda.__name__,
            'dict': {}
        }

        self.assertEqual(result, json.dumps(expexted, indent=4))

    def test_to_json_returns_correct_json_with_arguments(self):
        panda = Panda(
            name='Marto',
            age=20,
            weight=100.10,
            food=['bamboo', 'grass'],
            skills={'eat': 100, 'sleep': 200}
        )

        panda_result = panda.to_json(indent=4)
        panda_expexted = {
            'type': Panda.__name__,
            'dict': {
                'name': 'Marto',
                'age': 20,
                'weight': 100.10,
                'food': ['bamboo', 'grass'],
                'skills': {'eat': 100, 'sleep': 200}
            }
        }

        self.assertEqual(panda_result, json.dumps(panda_expexted, indent=4))

    def test_to_json_returns_correct_json_with_arguments_of_jsonable_type(self):
        panda = Panda(name='Marto', friend=Panda(name='Ivo'))

        panda_result = panda.to_json(indent=4)
        panda_expexted = {
            'type': Panda.__name__,
            'dict': {
                'name': 'Marto',
                'friend': {
                    'type': Panda.__name__,
                    'dict': {
                        'name': 'Ivo'
                    }
                }
            }
        }

        self.assertEqual(panda_result, json.dumps(panda_expexted, indent=4))

    def test_from_json_with_wrong_class_type(self):
        car = Car()
        car_json = car.to_json()

        with self.assertRaises(ValueError):
            Panda.from_json(car_json)

    def test_from_json_with_no_arguments(self):
        car = Car()
        car_json = car.to_json()

        result = Car.from_json(car_json)

        self.assertEqual(car, result)

    def test_from_json_with_arguments(self):
        panda = Panda(
            name='Marto',
            age=20,
            weight=100.10,
            food=['bamboo', 'grass'],
            skills={'eat': 100, 'sleep': 200}
        )
        panda_json = panda.to_json()

        result = Panda.from_json(panda_json)

        self.assertEqual(panda, result)


if __name__ == '__main__':
    unittest.main()
