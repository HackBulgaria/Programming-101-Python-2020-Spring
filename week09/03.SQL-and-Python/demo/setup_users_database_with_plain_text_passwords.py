import sqlite3


def create_users_table():
    connection = sqlite3.connect('users_with_plain_passwords.db')
    cursor = connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(50),
        password VARCHAR(100)
    )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def populate_users_table():
    users_data = []

    for i in range(100):
        users_data.append(
            f'("user_{i}", "password_{i}")'
        )

    connection = sqlite3.connect('users_with_plain_passwords.db')
    cursor = connection.cursor()
    query = f'''
        INSERT INTO users (username, password)
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
