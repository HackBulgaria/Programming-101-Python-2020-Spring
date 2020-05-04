from .controllers import UserContoller


class UserViews:
    def __init__(self):
        self.controller = UserContoller()

    def login(self):
        pass

    def signup(self):
        email = input('Email: ')
        password = input('Password: ')

        self.controller.create_user(email=email, password=password)
