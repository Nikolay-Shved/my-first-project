import random
START_SEQUENCE = 2
END_SEQUENCE = 100
GAME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def calculate(first_number):
    k = 0
    for i in range(2, first_number // 2 + 1):
        if (first_number % i == 0):
            k += 1
        if (k <= 0):
            return True


def get_question_and_answer():
    first_number = random.randint(START_SEQUENCE, END_SEQUENCE)
    correct_answer = calculate(first_number)
    if correct_answer == True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return f'{first_number}', correct_answer
