# TODO: Hash the passwords
CREATE_USERS = '''
    CREATE TABLE IF NOT EXISTS users (
        id integer PRIMARY KEY NOT NULL,
        email varchar(50) UNIQUE,
        password varchar(50)
    );
'''
