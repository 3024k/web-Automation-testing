from random import randint
import string
import  random

def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)

def id_generator(size = 5,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))