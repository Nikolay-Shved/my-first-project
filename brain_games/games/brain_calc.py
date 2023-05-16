import random
from random import choice

OPERATIONS = '+-*'
NUMBER_1 = 1
NUMBER_2 = 100


def calculation(rundom_number_1, rundom_number_2, rundom_operation):
    if rundom_operation == '+':
        result = rundom_number_1 + rundom_number_2
        return result
    elif rundom_operation == '-':
        result = rundom_number_1 - rundom_number_2
        return result
    else:
        result = rundom_number_1 * rundom_number_2
        return result


def game_body():
    rundom_number_1 = random.randint(NUMBER_1, NUMBER_2)
    rundom_number_2 = random.randint(NUMBER_1, NUMBER_2)
    rundom_operation = choice(OPERATIONS)
    result = calculation(rundom_number_1, rundom_number_2, rundom_operation)
    print(f'Question: {rundom_number_1} {rundom_operation} {rundom_number_2}')
    return result

