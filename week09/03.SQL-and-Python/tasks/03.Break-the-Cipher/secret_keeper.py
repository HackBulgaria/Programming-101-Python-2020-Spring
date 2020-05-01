import hashlib


def make_it_secret(message):
    return hashlib.md5(message.encode()).hexdigest()
