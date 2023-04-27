import random
from random import choice
from ..logic import congrats
from test import calculation


def calculations(result):
    counter = 3
    for i in range(counter):
        OPERATION = '+-*'
        NUM_1 = random.randint(1, 100)
        NUM_2 = random.randint(1, 100)
        NUM_3 = choice(OPERATION)

        answer = input('Your answer: ')

        if str(answer) == str(result):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            break

def calc_game(name):
    print(congrats(name, i))
