from datetime import datetime

from serializers import Serializer
from fields import CharField, EmailField, DateTimeField


class Panda:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = datetime.now()


class PandaSerializer(Serializer):
    name = CharField()
    email = EmailField()
    created_at = DateTimeField()


def main():
    panda = Panda('Ivo', 'ivo@hackbulgaria.com')
    serializer = PandaSerializer(instance=panda)

    serializer.is_valid()
    print(serializer.data)


if __name__ == '__main__':
    main()
