import hashlib


def make_it_secret_md5(password, count):
    for i in range(count):
        password = hashlib.md5(password.encode()).hexdigest()

    return password



def make_it_secret_sha512(password, count):
    for i in range(count):
        password = hashlib.sha512(password.encode()).hexdigest()

    return password
