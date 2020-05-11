from fields import Field


class DeclarativeSerializerMeta(type):
    def __new__(cls, name, bases, clsdict):
        fields = {}

        for attr, value in clsdict.items():
            if isinstance(value, Field):
                fields[attr] = value

        for attr, _ in fields.items():
            clsdict.pop(attr)

        clsdict['_fields'] = fields

        return super().__new__(cls, name, bases, clsdict)


class Serializer(metaclass=DeclarativeSerializerMeta):
    def __init__(self, instance):
        self._object = instance
        self._called_validation = False

    def is_valid(self):
        valid = True

        for field_name, field in self._fields.items():
            if not field.validate(getattr(self._object, field_name)):
                valid = False
                break

        self._called_validation = True
        return valid

    @property
    def data(self):
        if not self._called_validation:
            raise Exception('Call .is_valid() before .data')

        return { field_name: field.transform(getattr(self._object, field_name))
                 for field_name, field in self._fields.items() }
