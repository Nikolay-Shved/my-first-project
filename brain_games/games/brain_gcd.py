import random
import math
START_SEQUENCE = 1
END_SEQUENCE = 100
GAME_QUESTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    first_number = random.randint(START_SEQUENCE, END_SEQUENCE)
    second_number = random.randint(START_SEQUENCE, END_SEQUENCE)
    correct_answer = math.gcd(first_number, second_number)
    return f'{first_number} {second_number}', correct_answer
