class DeclarativeMeta(type):
    def __new__(cls, name, bases, clsdict):
        fields = {}

        for attr, value in clsdict.items():
            if not callable(value) and not attr.startswith('__'):
                fields[attr] = value

        for attr, _ in fields.items():
            clsdict.pop(attr)

        clsdict['_declared_fields'] = fields

        print(name, fields, clsdict, "=======================")
        clsobj = super().__new__(cls, name, bases, clsdict)

        return clsobj

class Base(metaclass=DeclarativeMeta):
    def __init__(self):
        for attr, value in self._declared_fields.items():
            setattr(self, attr, value)

    # def __getattr__(self, name):
    #     if name in self._declared_fields:
    #         return self._declared_fields[name]

    #     return object.__getattribute__(self, name)


class Panda(Base):
    a = 5
    b = 6


p1 = Panda()
p2 = Panda()

print(p1.a)
print(vars(p1))
print(p2.b)
print(p1.panda)
