import random
import math
START_SEQUENCE = 2
END_SEQUENCE = 100
GAME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def calculate(first_number):
    if first_number < 2:
        return False
    for i in range(2, int(math.sqrt(first_number)) + 1):
        if first_number % i == 0:
            return False
    return True


def get_question_and_answer():
    first_number = random.randint(START_SEQUENCE, END_SEQUENCE)
    correct_answer = calculate(first_number)
    correct_answer = 'yes' if calculate(first_number) else 'no'
    return f'{first_number}', correct_answer
