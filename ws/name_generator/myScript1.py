import random, string


def name_generator(name=''):
    for l in range(0, 3, 1):
        name += random.choice(string.ascii_lowercase)
    return name


print(name_generator())
