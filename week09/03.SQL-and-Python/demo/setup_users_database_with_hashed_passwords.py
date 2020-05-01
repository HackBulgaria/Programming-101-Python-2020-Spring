import sqlite3
import hashlib


def make_it_secret(password):
    return hashlib.sha512(password.encode()).hexdigest()


def create_users_table():
    connection = sqlite3.connect('users_with_hashed_passwords.db')
    cursor = connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(50),
        password VARCHAR(100),
        plain_text_password VARCHAR(100)
    )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def populate_users_table():
    users_data = []

    for i in range(100):
        plain_password = f'password_{i}'
        password = make_it_secret(plain_password)
        users_data.append(
            f'("user_{i}", "{password}", "{plain_password}")'
        )

    for i in range(100, 130):
        plain_password = 'qwerty'
        password = make_it_secret(plain_password)
        users_data.append(
            f'("user_{i}", "{password}", "{plain_password}")'
        )

    connection = sqlite3.connect('users_with_hashed_passwords.db')
    cursor = connection.cursor()
    query = f'''
        INSERT INTO users (username, password, plain_text_password)
          VALUES {','.join(users_data)}
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()



def main():
    create_users_table()
    populate_users_table()


if __name__ == '__main__':
    main()
