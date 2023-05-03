from ..logic import congrats
import random
from random import choice


def calculation():
        OPERATION = '+-*'
        NUM_1 = random.randint(1, 100)
        NUM_2 = random.randint(1, 100)
        NUM_3 = choice(OPERATION)
        print(f'Question: {NUM_1} {NUM_3} {NUM_2}')
        if NUM_3 == '+':
            result = NUM_1 + NUM_2
            return result
        elif NUM_3 == '-':
            result = NUM_1 - NUM_2
            return result
        else:
            result = NUM_1 * NUM_2
            return result


def calc_game(name):
    counter = 3
    for i in range(counter):
        result = calculation()
        answer = input('Your answer: ')

        if str(answer) == str(result):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            break
    print(congrats(name, i))
