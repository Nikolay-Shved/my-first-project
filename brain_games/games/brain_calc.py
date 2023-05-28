import random
from random import choice
OPERATIONS = '+-*'
START_SEQUENCE = 1
END_SEQUENCE = 100
GAME_QUESTION = 'What is the result of the expression?'


def calculate(first_number, second_number, operation):
    if operation == '+':
        correct_answer = first_number + second_number
        return correct_answer
    elif operation == '-':
        correct_answer = first_number - second_number
        return correct_answer
    else:
        correct_answer = first_number * second_number
        return correct_answer


def get_question_and_answer():
    first_number = random.randint(START_SEQUENCE, END_SEQUENCE)
    second_number = random.randint(START_SEQUENCE, END_SEQUENCE)
    operation = choice(OPERATIONS)
    correct_answer = calculate(first_number, second_number , operation)
    return (f'{first_number} {operation} {second_number }', correct_answer)
