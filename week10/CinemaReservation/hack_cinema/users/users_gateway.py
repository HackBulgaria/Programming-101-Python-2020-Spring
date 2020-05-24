from ..db import Database
from .models import UserModel


class UserGateway:
    def __init__(self):
        self.model = UserModel
        self.db = Database()

    def create(self, *, email, password):
        self.model.validate(email, password)

        self.db.cursor.execute()  # TODO: create user query

        # TODO: What whould I return?

    def all(self):
        raw_users = self.db.cursor.execute()  # TODO: Select all users

        return [self.model(**row) for row in raw_users]
