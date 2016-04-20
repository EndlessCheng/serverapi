import random
import string


def generate_token(randomlength=11):
    a = list(string.ascii_letters)
    random.shuffle(a)
    return ''.join(a[:randomlength])