import random

START_SEQUENCE = 1
END_SEQUENCE = 100
GAME_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(first_number):
    return first_number % 2 == 0


def get_question_and_answer():
    first_number = random.randint(START_SEQUENCE, END_SEQUENCE)
    correct_answer = is_even(first_number)
    correct_answer = 'yes' if is_even(first_number) else 'no'
    return f'{first_number}', correct_answer
