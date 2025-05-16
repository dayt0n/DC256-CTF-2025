import string
import random


def get_secret():
    random.seed("supersecretseed")
    letters = string.ascii_lowercase + string.ascii_uppercase
    return "".join([random.choice(letters) for a in range(16)])
