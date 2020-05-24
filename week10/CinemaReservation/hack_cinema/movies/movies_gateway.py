from hack_cinema.db import Database

from .models import Movie
from .queries import (
    CREATE_MOVIE,
    GET_ALL_MOVIES,
    GET_MOVIE,
    DELETE_MOVIE
)


class MovieGateway:
    def __init__(self):
        self.db = Database()
        self.model = Movie

    def create(self, title, year, rating):
        self.db.cursor.execute(CREATE_MOVIE, (title, year, rating))

        movie_id = self.db.cursor.lastrowid
        return self.get(movie_id)

    def get(self, id):
        self.db.cursor.execute(GET_MOVIE, (id, ))
        movie_row = self.db.cursor.fetchone()
        self.db.connection.commit()

        if not movie_row:
            raise ValueError(f'Movie with {id} not found.')

        return self.model(*movie_row)

    def all(self):
        self.db.cursor.execute(GET_ALL_MOVIES)
        movie_rows = self.db.cursor.fetchall()

        self.db.connection.commit()

        return [self.model(*row) for row in movie_rows]

    def filter(self, **kwargs):
        # TODO: Build where clauses here
        pass

    def delete(self, id):
        movie = self.get(id)  # make sure the movie exists before deleting it

        self.db.cursor.execute(DELETE_MOVIE, (id, ))
        self.db.connection.commit()

        return movie
