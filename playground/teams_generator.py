import random
import time
from pprint import pprint

STUDENT_NAMES = [
    'Tanya Budinova',
    'Иван Георгиев Гочев',
    'Ангелина Кръстанова',
    'Мария-Магдалена Желязкова',
    'Ралица Шиндарова',
    'Антонио Георгиев',
    'Silviya Vasileva Vasileva',
    'Християна Малинова',
    'Николай Колев Нешев',
    'Цветомир Цветков',
    'Петър Дамянов',
    'Георги Къков',
    'Николай Веселинов Късев',
    'Антони Стоев',
    'Златина Чолакова',
    'Снежина Лъчезарова Цанкова',
    'Димитър Николов',
    'Емилиан Спасов',
    'Йоанна Йотова',
    'Боян Бонев',
    'Георги Куклев',
    'Йоан Джелекарски',
    'Бойко Георгиев',
    'Redjep ',
    'Никола Методиев',
]

TEAM_NAMES = [
    'Panda',
    'Dog',
    'Cat',
    'Bear',
    'Horse',
    'Elephant',
    'Tiger',
    'Shark',
    'Owl',
    'Wolf',
    'Crocodile',
    'Lion'
]


def generate_teams():
    student_names = STUDENT_NAMES[:]

    for _ in range(10):
        random.shuffle(student_names)

    teams = [student_names[i:i + 2] for i in range(0, len(student_names), 2)]

    # The last team is from 3 students
    teams[-2].extend(teams[-1])
    del teams[-1]

    return {
        team_name: teams[index]
        for index, team_name in enumerate(TEAM_NAMES)
    }


if __name__ == '__main__':
    while True:
        result = generate_teams()
        pprint(result)
        time.sleep(0.1)
