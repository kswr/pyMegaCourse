import string, random

vowels="aeiouy"
consonants="bcdfghklmnpqrstvwxz"

matrix=""

for i in range(3):
    matrix = matrix+input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")

repeats=int(input("How many names do you want? "))

print(matrix)

def name():
    name=""
    for i in matrix:
        if i == 'v':
            name=name+random.choice(vowels)
        elif i == 'c':
            name=name+random.choice(consonants)
        else:
            name=name+random.choice(string.ascii_lowercase)
    return name

for i in range(repeats):
    print(name())
