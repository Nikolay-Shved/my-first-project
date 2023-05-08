from ..scripts.all_game import congrats
import random
from random import choice

OPERATIONS = '+-*'
rundom_number_1 = random.randint(1, 100)
rundom_number_2 = random.randint(1, 100)
rundom_operation = choice(OPERATIONS)


counter = 3
def calculation(rundom_number_1, rundom_number_2, rundom_operation):
        if rundom_operation == '+':
            result = rundom_number_1 + rundom_number_2
            return result
        elif rundom_operation == '-':
            result = rundom_number_1 - rundom_number_2
        else:
            result = rundom_number_1 * rundom_number_2
            return result


def calc_game(name):
    for i in range(counter):
        print(f'Question: {rundom_number_1} {rundom_operation} {rundom_number_2}')
        result = calculation(rundom_number_1, rundom_number_2, rundom_operation)
        answer = input('Your answer: ')

        if int(answer) == int(result):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            return print(f"Let's try again, {name}")
    congrats(name)
