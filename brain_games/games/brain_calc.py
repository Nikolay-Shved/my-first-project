import random
from random import choice
OPERATIONS = '+-*'
START_SEQUENCE = 1
END_SEQUENCE = 100
GAME_QUESTION = 'What is the result of the expression?'


def calculate(first_number, second_number, operation):
    if operation == '+':
        return first_number + second_number
    elif operation == '-':
        return first_number - second_number
    else:
        return first_number * second_number


def get_question_and_answer():
    first_number = random.randint(START_SEQUENCE, END_SEQUENCE)
    second_number = random.randint(START_SEQUENCE, END_SEQUENCE)
    operation = choice(OPERATIONS)
    correct_answer = calculate(first_number, second_number, operation)
    return (f'{first_number} {operation} {second_number }', correct_answer)
