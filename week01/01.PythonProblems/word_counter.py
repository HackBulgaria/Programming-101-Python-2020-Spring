def is_palindrome(word):
    return word == word[::-1]


def get_word_occurences(word, text):
    if is_palindrome(word):
        return text.count(word)

    return text.count(word) + text[::-1].count(word)


def build_matrix(rows, cols):
    matrix = []
    rows_inputted = 0
    print('Enter matrix: ')

    while rows_inputted < rows:
        row_input = input()

        row = row_input.strip().split(' ')
        if len(row) != cols:
            return 'Wrong input.'

        matrix.append(row)
        rows_inputted += 1

    return matrix


def word_occurances_in_rows(matrix, word):
    word_occurances = 0

    for row in matrix:
        word_occurances += get_word_occurences(word, ''.join(row))

    return word_occurances


def word_occurances_in_cols(matrix, word):
    word_occurances = 0
    cols_count = len(matrix[0])

    for i in range(cols_count):
        column = []
        for row in matrix:
            column.append(row[i])

        word_occurances += get_word_occurences(word, ''.join(column))

    return word_occurances


def word_occurances_in_right_diagonals(matrix, word):
    word_occurances = 0
    rows_count = len(matrix)
    cols_count = len(matrix[0])

    for c in range(rows_count + cols_count - 1):
        diagonal = []
        for i in range(rows_count):
            for j in range(cols_count):
                if i + j == c:
                    diagonal.append(matrix[i][j])

        word_occurances += get_word_occurences(word, ''.join(diagonal))

    return word_occurances


def word_occurances_in_left_diagonals(matrix, word):
    word_occurances = 0
    rows_count = len(matrix)
    cols_count = len(matrix[0])

    for c in range(1 - cols_count, rows_count):
        diagonal = []
        for i in range(rows_count):
            for j in reversed(range(cols_count)):
                if j - i == c:
                    diagonal.append(matrix[i][j])

        word_occurances += get_word_occurences(word, ''.join(diagonal))

    return word_occurances


def word_counter():
    word = input('Enter word: ')
    size = input('Enter matrix size (format: N M): ')

    n = int(size.split(' ')[0])
    m = int(size.split(' ')[1])

    if len(word) > min([n, m]):
        return 'Invalid number of rows or columns!'

    matrix = build_matrix(n, m)

    word_occurances = word_occurances_in_rows(matrix, word)
    word_occurances += word_occurances_in_cols(matrix, word)
    word_occurances += word_occurances_in_right_diagonals(matrix, word)
    word_occurances += word_occurances_in_left_diagonals(matrix, word)

    return word_occurances


if __name__ == '__main__':
    print(word_counter())
