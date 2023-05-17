import random
from random import choice

OPERATIONS = '+-*'
SEQUENCE_ELEMENT_1 = 1
SEQUENCE_ELEMENT_2 = 100


def expression(rundom_number_1, rundom_number_2, rundom_operation):
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
    rundom_number_1 = random.randint(SEQUENCE_ELEMENT_1, SEQUENCE_ELEMENT_2)
    rundom_number_2 = random.randint(SEQUENCE_ELEMENT_1, SEQUENCE_ELEMENT_2)
    rundom_operation = choice(OPERATIONS)
    result = expression(rundom_number_1, rundom_number_2, rundom_operation)
    return f'Question: {rundom_number_1} {rundom_operation} {rundom_number_2}', result
