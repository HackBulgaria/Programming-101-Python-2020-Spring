import sqlite3


def create_user(*, username, password):
    connection = sqlite3.connect('users_with_plain_passwords.db')
    cursor = connection.cursor()
    insert_query = f'''
    INSERT INTO users (username, password)
      VALUES ( ? , ? )
    '''
    cursor.execute(insert_query, (username, password))
    connection.commit()
    connection.close()


def main():
    while True:
        username = input('Username: ')
        password = input('Password: ')

        create_user(username=username, password=password)

        print('User registered successfully!!')


if __name__ == '__main__':
    main()
