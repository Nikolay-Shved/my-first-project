from ..scripts.all_game import congrats
import random
from random import choice

OPERATIONS = '+-*'
NUMBER_1 = 1
NUMBER_2 = 100


def calculation(random_number_1, random_number_2, random_operation):
    if random_operation == '+':
        result = random_number_1 + random_number_2
        return result
    elif random_operation == '-':
        result = random_number_1 - random_number_2
    else:
        result = random_number_1 * random_number_2
        return result


def calc_game(name):
    counter = 3
    for i in range(counter):
        random_number = random.randint(NUMBER_1, NUMBER_2)
        random_number_1 = random.randint(NUMBER_1, NUMBER_2)
        random_operation = choice(OPERATIONS)
        print(f'Question: {random_number}{random_operation}{random_number_1}')
        result = calculation(random_number, random_number_1, random_operation)
        answer = input('Your answer: ')

        if int(answer) == int(result):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            return print(f"Let's try again, {name}")
    congrats(name)
