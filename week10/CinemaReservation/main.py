import sys

from hack_cinema.db import Database
from hack_cinema.db_schema import CREATE_USERS, CREATE_MOVIES

from hack_cinema.index_view import welcome


class Application:
    @classmethod
    def build(self):
        db = Database()
        db.cursor.execute(CREATE_USERS)
        db.cursor.execute(CREATE_MOVIES)
        # TODO: Build rest of the tables

        db.connection.commit()
        db.connection.close()

        print('Done.')

    @classmethod
    def seed(self):
        # TODO: Seed with inistial data - consider using another command for this
        pass

    @classmethod
    def start(self):
        welcome()


if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'build':
        Application.build()
    elif command == 'seed':
        Application.start()
    elif command == 'start':
        Application.start()
    else:
        raise ValueError(f'Unknown command {command}. Valid ones are "build", "seed" and "start"')
