import random
from random import choice
OPERATIONS = '+-*'
START_SEQUENCE = 1
END_SEQUENCE = 100
GAME_QUESTION = 'What is the result of the expression?'


def calculate(start_of_sequence, end_of_sequence, operation):
    if operation == '+':
        correct_answer = start_of_sequence + end_of_sequence
        return correct_answer
    elif operation == '-':
        correct_answer = start_of_sequence - end_of_sequence
        return correct_answer
    else:
        correct_answer = start_of_sequence * end_of_sequence
        return correct_answer


def get_question_and_answer():
    first_number = random.randint(START_SEQUENCE, END_SEQUENCE)
    second_number = random.randint(START_SEQUENCE, END_SEQUENCE)
    operation = choice(OPERATIONS)
    correct_answer = calculate(first_number, second_number , operation)
    return (f'{first_number} {operation} {second_number }', correct_answer)
