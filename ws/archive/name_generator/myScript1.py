import random, string
'''I can finish my version of first app in the spare time'''

def name_generator(name=''):
    for l in range(30):
        name += random.choice(string.ascii_lowercase)
    return name


print(name_generator())
