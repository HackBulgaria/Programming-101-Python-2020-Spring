GET_ALL_MOVIES = 'SELECT * FROM movies'

CREATE_MOVIE = '''
    INSERT INTO movies (title, year, rating)
    VALUES (?, ?, ?);
'''

GET_MOVIE = '''
    SELECT *
    FROM movies
    WHERE id=?
'''

DELETE_MOVIE = 'DELETE FROM movies WHERE id=?'
