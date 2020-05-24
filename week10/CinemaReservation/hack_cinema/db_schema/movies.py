CREATE_MOVIES = '''
    CREATE TABLE IF NOT EXISTS movies(
        id INTEGER PRIMARY KEY,
        title VARCHAR(30) NOT NULL,
        year INTEGER NOT NULL CHECK(year BETWEEN 2019 and 2022),
        rating REAL CHECK(rating BETWEEN 0 and 10),
        UNIQUE(title, year)
    );
'''