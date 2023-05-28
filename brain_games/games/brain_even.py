import random

START_SEQUENCE = 1
END_SEQUENCE = 100
GAME_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def calculate(sequence_element):
    if sequence_element % 2 == 0:
        return 


def get_question_and_answer():
    first_number = random.randint(START_SEQUENCE, END_SEQUENCE)
    correct_answer = calculate(first_number)
    if correct_answer == True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return f'{first_number}', correct_answer
