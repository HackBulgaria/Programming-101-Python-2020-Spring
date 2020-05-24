class RegistryMeta(type):
    def __new__(cls, name, bases, clsdict):
        for base in bases:
            print(vars(base))
        clsobj = super().__new__(cls, name, bases, clsdict)
        print(clsobj)
        print('===========')

        if not hasattr(clsobj, 'registry'):
            clsobj.registry = []

        clsobj.registry.append(clsobj)

        return clsobj


class Base(metaclass=RegistryMeta):
    pass


class A(Base):
    pass


class B(Base):
    pass


print(Base.registry)
print(A.registry)
print(B.registry)
