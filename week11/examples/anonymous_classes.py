def create_mock_object(**kwargs):
    cls = type('', (object, ), {})
    obj = cls()

    for key, value in kwargs.items():
        setattr(obj, key, value)

    return obj
