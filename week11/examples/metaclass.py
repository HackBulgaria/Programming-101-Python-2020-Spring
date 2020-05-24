from class_decorators import debugmethods


class mytype(type):
    def __new__(cls, name, bases, clsdict):
        def m(self):
            print(self)
            print('in m')

        clsdict['m'] = m
        clsobj = super().__new__(cls, name, bases, clsdict)

        return clsobj

class mytype2(type):
    def __new__(cls, name, bases, clsdict):
        print('mytype2')
        clsobj = super().__new__(cls, name, bases, clsdict)

        return clsobj


class Base(metaclass=mytype):
    pass


class Base2(metaclass=mytype2):
    pass


class A(Base2, Base):
    pass


class B(A):
    pass


b = B()
b.m()
