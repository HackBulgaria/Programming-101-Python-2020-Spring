from .users_gateway import UserGateway


class UserContoller:
    def __init__(self):
        self.users_gateway = UserGateway()

    def create_user(self, email, password):
        user = self.users_gateway.create(email=email, password=password)

        return user

    def login_user(self, email, password):
        pass
