import random
import string


def generate_strong_password(length=12):

    characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    password = ''.join(random.choice(characters) for _ in range(length))

    return password
